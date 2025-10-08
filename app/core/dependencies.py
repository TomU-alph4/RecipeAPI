"""
Dependency injection functions for FastAPI endpoints.

These dependencies can be used across routes to inject common services,
configurations, and utilities into endpoint functions.
"""

from typing import Annotated
from fastapi import Header, HTTPException, status
from app.core.settings import settings
from app.core.logging import logger


# 1. Simple dependency: Get settings
def get_settings():
    """
    Returns the application settings.
    Useful for accessing configuration in endpoints.
    """
    return settings

