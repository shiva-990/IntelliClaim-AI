import re


def extract_policy_number(question: str):
    """
    Extract policy number from the user's question.

    Example:
        Does POL00017 cover flood damage?

    Returns:
        POL00017
    """

    pattern = r"POL\d{5}"

    match = re.search(
        pattern,
        question.upper()
    )

    if match:
        return match.group()

    return None