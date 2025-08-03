from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["system"])
def health_check():
    return {"status": "healthy", "version": "1.0.0"}
