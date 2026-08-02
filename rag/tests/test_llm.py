from rag.retriever.retriever import PolicyRetriever
from rag.llm.answer_generator import AnswerGenerator

retriever = PolicyRetriever()

documents = retriever.search(
    "Is bumper damage covered?"
)

generator = AnswerGenerator()

answer = generator.answer(
    "Is bumper damage covered?",
    documents,
)

print("=" * 60)
print(answer)
print("=" * 60)