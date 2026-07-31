import os

from dotenv import load_dotenv
from pinecone import Pinecone

from rag.config import PINECONE_INDEX

load_dotenv()


def get_pinecone_index():
    """
    Connect to Pinecone and return the index.
    """

    api_key = os.getenv("PINECONE_API_KEY")

    if not api_key:
        raise ValueError(
            "PINECONE_API_KEY not found in .env"
        )

    pc = Pinecone(api_key=api_key)

    index = pc.Index(PINECONE_INDEX)

    print("=" * 60)
    print("CONNECTED TO PINECONE")
    print("=" * 60)
    print(f"Index : {PINECONE_INDEX}")

    return index