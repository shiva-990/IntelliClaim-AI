from rag.llm.prompt_template import PROMPT_TEMPLATE
from rag.llm.qwen import QwenLLM


class AnswerGenerator:

    def __init__(self):

        self.llm = QwenLLM()

    def answer(
        self,
        question: str,
        documents,
    ):

        context = "\n\n".join(
            doc.page_content
            for doc in documents
        )

        prompt = PROMPT_TEMPLATE.format(
            context=context,
            question=question,
        )

        return self.llm.generate(prompt)