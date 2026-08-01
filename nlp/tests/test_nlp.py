from nlp.services.extractor import Extractor

extractor = Extractor()

text = """
A truck hit my car from the rear during heavy rain.
The rear bumper and tail light are damaged.
"""

result = extractor.extract(text)

print("=" * 60)

print(result)