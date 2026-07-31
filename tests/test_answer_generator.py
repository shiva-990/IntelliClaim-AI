from rag.llm.answer_generator import generate_answer


def main():

    context = """
Policy Number: POL00017

Coverage:
✓ Flood Damage
✓ Fire
✓ Theft
✓ Collision

Claim Limit:
₹4,50,000

Waiting Period:
None
"""

    question = "Does my policy cover flood damage?"

    answer = generate_answer(
        context=context,
        question=question
    )

    print("\n")
    print("=" * 60)
    print("FINAL ANSWER")
    print("=" * 60)
    print(answer)


if __name__ == "__main__":
    main()