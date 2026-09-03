from ingest import load_documents, chunk_document
from retriever import embed_and_store, get_collection

# Clear/check collection state
collection = get_collection()
print(f"Current collection count before store: {collection.count()}")

# Load and chunk docs
documents = load_documents()
all_chunks = []
for doc in documents:
    chunks = chunk_document(doc["text"], doc["source"])
    all_chunks.extend(chunks)

# Store in ChromaDB
if all_chunks:
    embed_and_store(all_chunks)
    print(f"Successfully stored {len(all_chunks)} chunks!")
else:
    print("No chunks found to store.")