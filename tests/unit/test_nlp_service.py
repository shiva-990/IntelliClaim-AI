from services.nlp_service import NLPService


def test_nlp_service():

    text = """
    My Honda City was hit from behind by a bike during heavy rain.
    """

    result = NLPService.analyze_claim(text)

    print(result)


if __name__ == "__main__":
    test_nlp_service() 