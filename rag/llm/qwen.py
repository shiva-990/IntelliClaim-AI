from langchain_ollama import ChatOllama


class QwenLLM:

    def __init__(self):

        self.llm = ChatOllama(
            model="qwen2.5:7b",   # We'll adjust this if your model name differs
            temperature=0,
        )

    def generate(
        self,
        prompt: str,
    ):

        response = self.llm.invoke(prompt)

        return response.content