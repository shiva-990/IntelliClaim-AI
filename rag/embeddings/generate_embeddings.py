import json

from rag.documents.loader import load_policy_documents
from rag.documents.splitter import split_documents
from rag.embeddings.embedding_model import get_embedding_model

from rag.config import PROJECT_ROOT


# ==========================================================
# GENERATE EMBEDDINGS
# ==========================================================

def generate_embeddings(chunks):

    embedding_model = get_embedding_model()

    print("\nGenerating embeddings...\n")

    vectors = []

    for i, chunk in enumerate(chunks, start=1):

        embedding = embedding_model.embed_query(
            chunk.page_content
        )

        vectors.append(
            {
                "id": f"chunk_{i}",
                "embedding": embedding,
                "metadata": chunk.metadata,
                "content": chunk.page_content,
            }
        )

        if i % 10 == 0:
            print(f"Processed {i}/{len(chunks)} chunks")

    return vectors


# ==========================================================
# SAVE
# ==========================================================

def save_embeddings(vectors):

    output_folder = PROJECT_ROOT / "outputs"

    output_folder.mkdir(exist_ok=True)

    output_file = output_folder / "policy_embeddings.json"

    with open(output_file, "w", encoding="utf-8") as f:

        json.dump(
            vectors,
            f,
            indent=2,
            ensure_ascii=False,
        )

    print("\nEmbeddings saved successfully.")

    print(output_file)


# ==========================================================
# PREVIEW
# ==========================================================

def preview(vectors):

    first = vectors[0]

    print("\n" + "=" * 60)
    print("EMBEDDING PREVIEW")
    print("=" * 60)

    print("ID:", first["id"])

    print("Policy:", first["metadata"]["policy_number"])

    print("Vector Dimension:", len(first["embedding"]))

    print("\nFirst 10 Values:")

    print(first["embedding"][:10])


# ==========================================================
# MAIN
# ==========================================================

def main():

    docs = load_policy_documents()

    chunks = split_documents(docs)

    vectors = generate_embeddings(chunks)

    preview(vectors)

    save_embeddings(vectors)

    print("\n" + "=" * 60)
    print("B4 COMPLETED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    main()