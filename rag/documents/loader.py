from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader


class PolicyLoader:

    def __init__(self, documents_path: Path):

        self.documents_path = documents_path

    def load_documents(self):

        documents = []

        pdf_files = sorted(
            self.documents_path.glob("*.pdf")
        )

        for pdf in pdf_files:

            loader = PyPDFLoader(str(pdf))

            pages = loader.load()

            for page in pages:

                page.metadata["policy_number"] = pdf.stem

            documents.extend(pages)

        return documents