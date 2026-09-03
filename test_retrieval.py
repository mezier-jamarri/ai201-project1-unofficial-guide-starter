from retriever import retrieve

# Test query based on our Milestone 2 evaluation plan
query = "striker channel firing pin lubrication"

print(f"Testing query: '{query}'\n" + "="*50)
results = retrieve(query)

if not results:
    print("No results returned. Is your vector store populated? Run ingest.py first!")
else:
    for i, res in enumerate(results):
        print(f"\nRESULT {i+1}")
        print(f"Source Document : {res['source']}")
        print(f"Distance Score  : {res['distance']:.4f} (Lower = Better)")
        print(f"Text Snippet    : {res['text']}")
        print("-" * 50)