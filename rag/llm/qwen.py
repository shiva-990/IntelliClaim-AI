from langchain_groq import ChatGroq
from configs.settings import settings


class QwenLLM:

    def __init__(self):

        self.llm = ChatGroq(
            api_key=settings.GROQ_API_KEY,
            model="llama-3.1-8b-instant",
            temperature=0,
        )

    def generate(self, prompt: str):

        response = self.llm.invoke(prompt)

        return response.content