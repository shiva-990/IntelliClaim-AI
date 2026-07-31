from rag.llm.qwen import get_llm


def main():

    llm = get_llm()

    response = llm.invoke(
        "Explain vehicle insurance in one sentence."
    )

    print("\n")
    print("=" * 60)
    print("QWEN RESPONSE")
    print("=" * 60)
    print(response.content)


if __name__ == "__main__":
    main()