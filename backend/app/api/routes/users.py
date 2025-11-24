from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from app.crud.user import (
    create_user,
    get_user_by_id,
    get_user_by_name,
    get_user_by_email,
    get_user_by_role,
    get_users,
    update_user,
    delete_user
)
from app.schemas import user as schemas
from app.api.deps import SessionDep, get_current_active_superuser, CurrentUser
from app.crud.exeptions.not_authorised import UserNotAuthorised


router = APIRouter()

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/register", response_model=schemas.User)
def register_user(db: SessionDep, user: schemas.UserCreate):
    return create_user(db=db, user=user)


@router.get("/{user_id}", response_model=schemas.User)
def get_user(db: SessionDep, user_id: int, user: CurrentUser):
    try:
        return get_user_by_id(db=db, user_id=user_id, user=user)
    except UserNotAuthorised:
        raise HTTPException(status_code=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION, detail="User not authorised for this operation")


@router.get(
    "/",
    dependencies=[Depends(get_current_active_superuser)],
    response_model=List[schemas.User],
)
# @router.get("/", response_model=List[schemas.User])
def get_users(db: SessionDep):
    return crud.get_users(db=db)
