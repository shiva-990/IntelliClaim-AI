from rag.config import POLICY_PDF_DIR

print("=" * 50)

print("Policy Folder")

print(POLICY_PDF_DIR)

print()

print("Exists :", POLICY_PDF_DIR.exists())

print()

print("PDF Count :", len(list(POLICY_PDF_DIR.glob("*.pdf"))))

print("=" * 50)