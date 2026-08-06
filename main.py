from fastapi import FastAPI
from configs.settings import settings
from exceptions import register_exception_handlers
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="IntelliClaim AI",
    version="1.0.0",
    description="AI Powered Insurance Claim Processing"
)
register_exception_handlers(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Welcome to IntelliClaim AI"}

@app.get("/config-test")
def config_test():
    return {
        "database": settings.DATABASE_URL,
        "ollama": settings.OLLAMA_MODEL,
        "pinecone": settings.PINECONE_INDEX_NAME
    }

# Include your routers after this
from api.v1 import api_v1_router

app.include_router(api_v1_router)