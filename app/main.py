from fastapi import FastAPI
from app.core.logging import logger
import os

app = FastAPI()

logger.info("Application started")

@app.get("/")
def read_root():
    logger.info("Root endpoint accessed")
    return {"message": "Hello World"}

@app.get("/health")
def health_check():
    return {"status": "Healthy"}