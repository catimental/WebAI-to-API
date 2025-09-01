# src/app/middleware/auth.py
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.config import get_allowed_key

security = HTTPBearer(auto_error=False)

async def verify_api_key(request: Request, call_next):
    """Middleware to verify API key from Authorization header or X-API-Key header."""
    allowed_key = get_allowed_key()
    
    if not allowed_key:
        # If no ALLOWED_KEY is configured, allow all requests
        return await call_next(request)
    
    # Check Authorization header
    api_key_header = request.headers.get("X-API-Key")
    
    provided_key = None
    
    if api_key_header:
        provided_key = api_key_header
    
    if not provided_key or provided_key != allowed_key:
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing API key"
        )
    
    return await call_next(request)