from nlp.models.preprocess import TextPreprocessor
from nlp.models.extractor import ClaimInformationExtractor


def test_extractor():

    text = """
    My Honda City was hit from behind during heavy rain.
    """

    cleaned = TextPreprocessor.clean(text)

    result = ClaimInformationExtractor.extract(cleaned)

    print(result)


if __name__ == "__main__":
    test_extractor() 