from rag.documents.loader import load_policy_documents
from rag.documents.splitter import split_documents
from rag.embeddings.embedding_model import get_embedding_model
from rag.vector_store.pinecone_store import get_pinecone_index


def upload_vectors():

    docs = load_policy_documents()

    chunks = split_documents(docs)

    embeddings = get_embedding_model()

    index = get_pinecone_index()

    vectors = []

    for i, chunk in enumerate(chunks):
        print("=" * 60)
        print(chunk.metadata)
        print("=" * 60)
        vector = embeddings.embed_documents(
           [chunk.page_content]
        )[0]

        vectors.append(
            {
                "id": f"chunk_{i}",
                "values": vector,
                "metadata": {
                    **chunk.metadata,
                    "text": chunk.page_content
                }
            }
        )

    print(f"\nUploading {len(vectors)} vectors...\n")

    batch_size = 50

    for start in range(0, len(vectors), batch_size):

        end = start + batch_size

        index.upsert(vectors=vectors[start:end])

        print(f"Uploaded {min(end, len(vectors))}/{len(vectors)}")

    print("\nUpload completed successfully.")


if __name__ == "__main__":
    upload_vectors()