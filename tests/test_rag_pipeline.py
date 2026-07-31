from rag.rag_pipeline import ask_question


def main():

    question = input("Ask a question: ")

    answer = ask_question(question)

    print("\n")
    print("=" * 70)
    print("INTELLICLAIM AI")
    print("=" * 70)
    print(answer)


if __name__ == "__main__":
    main()