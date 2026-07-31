from functools import lru_cache
from langchain_ollama import ChatOllama


@lru_cache(maxsize=1)
def get_llm():
    print("=" * 60)
    print("LOADING QWEN LLM")
    print("=" * 60)

    llm = ChatOllama(
        model="qwen2.5:7b",
        temperature=0,
    )

    print("Qwen loaded successfully.")

    return llm