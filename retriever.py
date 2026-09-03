import chromadb
from chromadb.utils import embedding_functions
from config import CHROMA_COLLECTION, CHROMA_PATH, EMBEDDING_MODEL, N_RESULTS

# Initialize the local sentence-transformer embedding model.
_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name=EMBEDDING_MODEL
)

# Initialize a persistent ChromaDB client saving to disk at ./chroma_db
_client = chromadb.PersistentClient(path=CHROMA_PATH)

# Get or create our collection. 
# We pass embedding_function=_ef, and cast it as Any to satisfy Pylance's strict type checker.
_collection = _client.get_or_create_collection(
    name=CHROMA_COLLECTION,
    embedding_function=_ef, # type: ignore
    metadata={"hnsw:space": "cosine"},
)


def get_collection():
    """Return the ChromaDB collection. Used by app.py during startup ingestion."""
    return _collection


def embed_and_store(chunks):
    """
    Embed a list of chunks and store them in the ChromaDB vector database.
    """
    if not chunks:
        print("No chunks provided to store.")
        return

    _collection.add(
        documents=[c["text"] for c in chunks],
        metadatas=[{"source": c["source"]} for c in chunks],
        ids=[c["chunk_id"] for c in chunks],
    )
    print(f"Successfully embedded and stored {_collection.count()} chunks in ChromaDB.")


def retrieve(query, n_results=N_RESULTS):
    """
    Find the most relevant rule chunks for a user's question via semantic search.
    """
    if _collection.count() == 0:
        print("Warning: Vector store is empty. Run ingestion first.")
        return []

    # Run semantic search against the collection
    results = _collection.query(
        query_texts=[query],
        n_results=n_results,
        include=["documents", "metadatas", "distances"]
    )

    retrieved_chunks = []
    
    # Safely check that results and inner keys are not None before subscripting
    if results and results.get("documents") and results["documents"] is not None:
        docs_list = results["documents"]
        metas_list = results.get("metadatas")
        dists_list = results.get("distances")

        if len(docs_list) > 0 and docs_list[0] is not None:
            docs = docs_list[0]
            metadatas = metas_list[0] if metas_list and metas_list[0] is not None else [{}] * len(docs)
            distances = dists_list[0] if dists_list and dists_list[0] is not None else [0.0] * len(docs)

            for doc, meta, dist in zip(docs, metas_list[0] if metas_list else [], dists_list[0] if dists_list else []):
                retrieved_chunks.append({
                    "text": doc,
                    "source": meta.get("source", "Unknown") if meta else "Unknown",
                    "distance": dist
                })

    return retrieved_chunks