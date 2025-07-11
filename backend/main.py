import os
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.database import test_db


app = FastAPI(
    title="RAG FastAPI Backend",
    description="A FastAPI backend for a Retrieval-Augmented Generation (RAG) application.",
    version="1.0.0",

    openapi_security=[{
        "bearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }]
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    """
    Startup event to test database connection.
    Also, download the model if not already downloaded.
    """
    try:
        test_db()
        logging.info("✅ Database connection successful. ✅")
    except Exception as e:
        logging.error(f"❌ Database connection failed: {e} ❌")
        raise e
    
    try:
        if os.path.exists("distilgpt2") and os.path.exists("all-MiniLM-L6-v2"):
            logging.info("Models already downloaded.")
        else:
            from rag_models.download_models import download_models
            download_models()
            logging.info("All models downloaded successfully.")
    except Exception as e:
        logging.error(f"❌ Model download failed: {e} ❌")
        raise Exception("Model download failed. Delete the model folders and restart the server to re-download them.")


@app.get("/")
async def read_root():
    """Root endpoint."""
    return {"message": "Welcome to the RAG FastAPI Backend!"}


from tasks.worker import celery_app, add

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    db_check = False
    try: 
        test_db()
        db_check = True
    except Exception as e:
        logging.error(f"❌ Database connection failed: {e} ❌")
    
    celery_check = False
    try:
        result = add.delay(1, 2) 
        celery_app.control.ping() 
        logging.info(f"Celery task result: {result.get(timeout=5)}")
        if result.ready():
            logging.info("✅ Celery task completed successfully. ✅")
        celery_check = True
    except Exception as e:
        logging.error(f"❌ Celery connection failed: {e} ❌")
    return {
        "fastapi": "running",
        "database": "connected" if db_check else "disconnected",
        "celery": "connected" if celery_check else "disconnected"
    }