from fastapi import APIRouter, Depends
from .dependencies import require_admin

router = APIRouter()

@router.get("/admin/dashboard", dependencies=[Depends(require_admin)])
def admin_dashboard():
    return {"message": "Admin data"}