import os
import re
from config import DOCS_PATH

def load_documents():
    """Load all .txt cleaning guides and forum threads from the docs folder."""
    documents = []
    
    if not os.path.exists(DOCS_PATH):
        print(f"Directory {DOCS_PATH} not found. Please create it and add your 10 txt files.")
        return documents
        
    for filename in sorted(os.listdir(DOCS_PATH)):
        if filename.endswith(".txt"):
            filepath = os.path.join(DOCS_PATH, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()
            
            # Use the filename as the source name (e.g., "glock_official_guide")
            source_name = filename.replace(".txt", "").replace("_", " ").title()
            documents.append({
                "source": source_name, # Changed "game" to "source" for our new domain
                "filename": filename,
                "text": text,
            })
    print(f"Loaded {len(documents)} document(s): {[d['source'] for d in documents]}")
    return documents

def clean_text(text):
    """Normalize whitespace to prevent empty/wasted characters in chunks."""
    text = re.sub(r'<[^>]+>', '', text) # Strip stray HTML if scraped
    text = re.sub(r'\s+', ' ', text).strip() # Compress multiple spaces/newlines
    return text

def chunk_document(text, source_name):
    """
    Split a document into chunks ready for embedding based on our Milestone 2 spec.
    
    Strategy: character-based sliding window with overlap.
      - chunk_size = 800: Large enough to capture a full multi-step cleaning instruction 
        or complete forum comment without splitting the context.
      - overlap = 150: Ensures that a step spanning two chunks retains the component 
        name (e.g., "slide rails") from the previous chunk.
    """
    # Updated to match planning.md specs
    chunk_size = 800
    overlap = 150
    min_length = 100 # Increased slightly since chunks are much larger now

    chunks = []
    prefix = source_name.lower().replace(" ", "_")
    counter = 0

    # Clean the raw text before chunking
    cleaned_text = clean_text(text)

    start = 0
    while start < len(cleaned_text):
        end = start + chunk_size
        chunk_text = cleaned_text[start:end].strip()

        if len(chunk_text) >= min_length:
            chunks.append({
                "text": chunk_text,
                "source": source_name, 
                "chunk_id": f"{prefix}_{counter}",
            })
            counter += 1

        start += chunk_size - overlap

    return chunks

if __name__ == "__main__":
    print("Starting ingestion test...\n")
    
    # 1. Load the documents
    docs = load_documents()
    
    all_chunks = []
    # 2. Chunk each document
    for doc in docs:
        chunks = chunk_document(doc["text"], doc["source"])
        all_chunks.extend(chunks)
        
    print(f"\nTotal chunks created: {len(all_chunks)}")
    print("-" * 40)
    
    # 3. Print the first 5 chunks for inspection
    for i in range(min(5, len(all_chunks))):
        print(f"CHUNK {i+1} (Source: {all_chunks[i]['source']}):")
        print(all_chunks[i]['text'])
        print("-" * 40)