from rag.retriever.retriever import PolicyRetriever

retriever = PolicyRetriever()

results = retriever.search(
    "Is bumper damage covered?"
)

print("=" * 60)
print("Retrieved Chunks :", len(results))
print("=" * 60)

for i, doc in enumerate(results, start=1):

    print(f"\nResult {i}")
    print("-" * 40)

    print("Policy :", doc.metadata["policy_number"])
    print("Page   :", doc.metadata["page"])

    print()

    print(doc.page_content[:500])