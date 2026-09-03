import gradio as gr
from config import DOCS_PATH
from ingest import load_documents, chunk_document
from retriever import get_collection, embed_and_store
from generator import generate_answer

def initialize_database():
    """Ensure the vector database is populated on app startup."""
    collection = get_collection()
    if collection.count() == 0:
        print("Vector store is empty. Running initial ingestion...")
        docs = load_documents()
        all_chunks = []
        for doc in docs:
            chunks = chunk_document(doc["text"], doc["source"])
            all_chunks.extend(chunks)
        if all_chunks:
            embed_and_store(all_chunks)
        print(f"Initialized database with {collection.count()} chunks.")
    else:
        print(f"Vector store already contains {collection.count()} chunks.")

def handle_query(question):
    """
    Process the user query through our RAG pipeline:
    1. Retrieve relevant chunks & generate a grounded answer via Groq.
    2. Format sources cleanly for the UI.
    """
    if not question.strip():
        return "Please enter a valid question.", "None"
    
    result = generate_answer(question)
    
    answer = result["answer"]
    sources = result["sources"]
    
    if sources:
        formatted_sources = "\n".join(f"• {src}" for src in sources)
    else:
        formatted_sources = "None (No sources cited)"
        
    return answer, formatted_sources

# Initialize database before launching UI
initialize_database()

# Build the Gradio Blocks Interface
with gr.Blocks(title="The Unofficial Guide: Handgun Maintenance") as demo:
    gr.Markdown("# 🛡️ The Unofficial Guide: Handgun Maintenance")
    gr.Markdown("Ask any question about cleaning, stripping, or lubricating your striker-fired handgun. Answers are strictly grounded in our curated collection of guides and community discussions.")
    
    with gr.Row():
        with gr.Column():
            inp = gr.Textbox(label="Your Question", placeholder="e.g., How often should I lubricate my Glock?", lines=2)
            btn = gr.Button("Ask Question", variant="primary")
            
        with gr.Column():
            answer_box = gr.Textbox(label="Grounded Answer", lines=8)
            sources_box = gr.Textbox(label="Retrieved From (Sources)", lines=4)

    # Wire up interactions explicitly passing arguments to satisfy type checkers
    btn.click(fn=handle_query, inputs=[inp], outputs=[answer_box, sources_box])
    inp.submit(fn=handle_query, inputs=[inp], outputs=[answer_box, sources_box])

if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", server_port=7860)