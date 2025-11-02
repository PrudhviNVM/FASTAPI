from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/")
def get_users():
    return {"users": ["user1", "user2", "user3"]}

@router.get("/{user_id}")
def get_user(user_id: int):
    return {"message": f"User {user_id} details"}