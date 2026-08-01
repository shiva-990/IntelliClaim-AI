from nlp.models.preprocess import TextPreprocessor
from nlp.models.classifier import ClaimClassifier


def test_classifier():

    text = """
    My Honda City was hit from behind by a bike during heavy rain.
    """

    cleaned = TextPreprocessor.clean(text)

    result = ClaimClassifier.classify(cleaned)

    print(result)


if __name__ == "__main__":
    test_classifier() 