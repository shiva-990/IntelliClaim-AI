import json

from langchain_text_splitters import RecursiveCharacterTextSplitter

from rag.config import (
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    PROJECT_ROOT,
)

from rag.documents.loader import load_policy_documents


# ==========================================================
# SPLIT DOCUMENTS
# ==========================================================

def split_documents(documents):
    """
    Split loaded PDF documents into overlapping chunks.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            ""
        ],
        length_function=len,
    )

    chunks = splitter.split_documents(documents)

    print("=" * 60)
    print("TEXT CHUNKING")
    print("=" * 60)

    print(f"Original Pages : {len(documents)}")
    print(f"Chunks Created : {len(chunks)}")

    return chunks


# ==========================================================
# PREVIEW CHUNKS
# ==========================================================

def preview_chunks(chunks, num_chunks=3):
    """
    Preview the first few chunks.
    """

    print("\n" + "=" * 60)
    print("CHUNK PREVIEW")
    print("=" * 60)

    for i, chunk in enumerate(chunks[:num_chunks], start=1):

        print(f"\nChunk {i}")
        print("-" * 60)

        print("Metadata:")

        for key, value in chunk.metadata.items():
            print(f"{key} : {value}")

        print("\nCharacters :", len(chunk.page_content))

        print("\nContent:\n")

        print(chunk.page_content)

        print("\n" + "=" * 60)


# ==========================================================
# SAVE CHUNKS
# ==========================================================

def save_chunks(chunks):
    """
    Save chunks into JSON for inspection/debugging.
    """

    output_folder = PROJECT_ROOT / "outputs"

    output_folder.mkdir(parents=True, exist_ok=True)

    output_file = output_folder / "policy_chunks.json"

    chunk_data = []

    for i, chunk in enumerate(chunks):

        chunk_data.append(
            {
                "chunk_id": i + 1,
                "content": chunk.page_content,
                "metadata": chunk.metadata,
                "length": len(chunk.page_content),
            }
        )

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(
            chunk_data,
            f,
            indent=4,
            ensure_ascii=False,
        )

    print("\nChunks saved successfully.")

    print(output_file)


# ==========================================================
# CHUNK STATISTICS
# ==========================================================

def print_statistics(chunks):
    """
    Print chunk statistics.
    """

    lengths = [len(chunk.page_content) for chunk in chunks]

    print("\n" + "=" * 60)
    print("CHUNK STATISTICS")
    print("=" * 60)

    print(f"Total Chunks     : {len(chunks)}")
    print(f"Minimum Length   : {min(lengths)}")
    print(f"Maximum Length   : {max(lengths)}")
    print(f"Average Length   : {sum(lengths)//len(lengths)}")

    print("=" * 60)


# ==========================================================
# MAIN
# ==========================================================

def main():

    print("=" * 60)
    print("INTELLICLAIM AI - DOCUMENT CHUNKING")
    print("=" * 60)

    documents = load_policy_documents()

    chunks = split_documents(documents)

    preview_chunks(chunks)

    save_chunks(chunks)

    print_statistics(chunks)

    print("\n" + "=" * 60)
    print("B3 COMPLETED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    main()