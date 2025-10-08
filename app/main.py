from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.core.settings import settings, Settings
from app.core.logging import logger
from app.core.dependencies import get_settings

app = FastAPI(
    title=settings.app_name,
    description=settings.app_description,
    version=settings.app_version,
    contact={"name": settings.app_contact, "url": settings.app_license_url, "email": settings.app_contact},
    license_info={"name": settings.app_license, "url": settings.app_license_url},
    terms_of_service=settings.app_terms_of_service,
)

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.get("/health")
def health_check():
    return {"message": "The API is running 😀"}


# Example 1: Using settings dependency
@app.get("/info")
def get_app_info(app_settings: Settings = Depends(get_settings)):
    """
    Demonstrates injecting settings into an endpoint.
    """
    return {
        "app_name": app_settings.app_name,
        "version": app_settings.app_version,
        "description": app_settings.app_description
    }
