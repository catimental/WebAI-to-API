# src/app/middleware/dependencies.py
from fastapi import Header, HTTPException, Depends
from typing import Optional
from app.config import get_allowed_key

def verify_api_key_dependency(x_api_key: Optional[str] = Header(None)):
    """Dependency to verify API key from X-API-Key header."""
    allowed_key = get_allowed_key()
    
    if not allowed_key:
        # If no ALLOWED_KEY is configured, allow all requests
        return True
    
    if not x_api_key or x_api_key != allowed_key:
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing API key"
        )
    
    return True