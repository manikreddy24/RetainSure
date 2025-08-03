@router.get("/search", response_model=List[UserResponse])
def search_users(
    name: str = Query(..., min_length=2),
    db: Session = Depends(get_db)
):
    return (
        db.query(User)
        .filter(User.username.ilike(f"%{name}%"))
        .limit(10)
        .all()
    )