from fastapi import Depends, HTTPException, status
from .security import get_current_user

async def require_admin(user: User = Depends(get_current_user)):
    if user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")