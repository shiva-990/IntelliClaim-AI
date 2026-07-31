from rag.retriever.pinecone_retriever import retrieve_documents


def main():

    print("=" * 60)
    print("INTELLICLAIM AI - POLICY RETRIEVER")
    print("=" * 60)

    while True:

        query = input("\nAsk a policy question (type 'exit' to quit): ")

        if query.lower() == "exit":
            break

        results = retrieve_documents(query)

        print("\n" + "=" * 60)
        print("TOP MATCHES")
        print("=" * 60)

        for i, match in enumerate(results["matches"], start=1):

            metadata = match["metadata"]

            print(f"\nMatch {i}")
            print("-" * 50)

            print(f"Score          : {match['score']:.4f}")
            print(f"Policy Number  : {metadata.get('policy_number')}")
            print(f"Page           : {metadata.get('page') + 1}")
            print(f"Source         : {metadata.get('source')}")

            print("\nContent:\n")

            print(metadata.get("text"))

            print("\n" + "=" * 60)


if __name__ == "__main__":
    main()