from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.schemas.post import PostCreate, PostResponse
from app.services.post import PostService, get_post_service
from app.core.security import get_current_user

router = APIRouter()


@router.post("/", response_model=int)
def add_post(post: PostCreate, current_user: int = Depends(get_current_user),
             post_service: PostService = Depends(get_post_service)):
    return post_service.add_post(post, current_user)


@router.get("/", response_model=List[PostResponse])
def get_posts(current_user: int = Depends(get_current_user), post_service: PostService = Depends(get_post_service)):
    return post_service.get_posts(current_user)


@router.delete("/{post_id}", response_model=None)
def delete_post(post_id: int, current_user: int = Depends(get_current_user),
                post_service: PostService = Depends(get_post_service)):
    post_service.delete_post(post_id, current_user)
    return None
