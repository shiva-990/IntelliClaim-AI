from nlp.models.preprocess import TextPreprocessor


def test_preprocess():
    text = "My Honda City was HIT from behind!! It happened during HEAVY rain."

    cleaned = TextPreprocessor.clean(text)

    print(cleaned)


if __name__ == "__main__":
    test_preprocess() 