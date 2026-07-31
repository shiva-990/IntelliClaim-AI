from rag.llm.qwen import get_llm
from rag.llm.prompt_template import get_prompt_template


def generate_answer(context: str, question: str):

    llm = get_llm()

    prompt = get_prompt_template()

    messages = prompt.format_messages(
        context=context,
        question=question
    )

    response = llm.invoke(messages)

    return response.content.strip()