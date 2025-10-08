import pydantic_settings

class Settings(pydantic_settings.BaseSettings):
    # App Configuration
    app_name: str = "RecipeAPI"
    app_description: str = "A FastAPI-based backend that scans grocery receipts, extracts purchased ingredients using OCR + NLP, stores them in PostgreSQL, and recommends recipes the user can cook with what they already have."
    app_version: str = "0.1.0"
    app_contact: str = "tomuns2000@hotmail.co.uk"
    app_license: str = "MIT"
    app_license_url: str = "https://opensource.org/licenses/MIT"
    app_terms_of_service: str = "https://opensource.org/licenses/MIT"
    
    # Database Configuration
    database_url: str = "postgresql://postgres:password@localhost:5432/recipeapi"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()