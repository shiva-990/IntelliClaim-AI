from rag.llm.prompt_template import get_prompt_template


def main():

    prompt = get_prompt_template()

    formatted = prompt.format_messages(
        context="""
Policy Number: POL00017

Coverage:
✓ Flood Damage
✓ Fire
✓ Theft
✓ Collision
""",
        question="Does my policy cover flood damage?"
    )

    print(formatted[0].content)


if __name__ == "__main__":
    main()