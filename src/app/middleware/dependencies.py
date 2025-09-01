
# src/app/middleware/dependencies.py
from fastapi import Header, HTTPException, Depends
from typing import Optional
from app.config import get_allowed_key

def verify_api_key_dependency(authorization: Optional[str] = Header(None)):
    """Dependency to verify API key from Authorization Bearer header."""
    allowed_key = get_allowed_key()
    
    if not allowed_key:
        # If no ALLOWED_KEY is configured, allow all requests
        return True
    
    # Check Authorization header (Bearer token)
    provided_key = None
    if authorization and authorization.startswith("Bearer "):
        provided_key = authorization[7:]  # Remove "Bearer " prefix
    
    if not provided_key or provided_key != allowed_key:
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing API key. Use Authorization: Bearer <key>"
        )
    
    return True