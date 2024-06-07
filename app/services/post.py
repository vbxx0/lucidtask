from sqlalchemy.orm import Session
from fastapi import Depends
from typing import List
from app.core.database import SessionLocal
from app.models.post import Post
from app.schemas.post import PostCreate
from fastapi import HTTPException, status
from cachetools import TTLCache

post_cache = TTLCache(maxsize=100, ttl=300)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_post_service(db: Session = Depends(get_db)):
    return PostService(db)


class PostService:
    def __init__(self, db: Session):
        self.db = db

    def add_post(self, post: PostCreate, user_id: int):
        db_post = Post(text=post.text, owner_id=user_id)
        self.db.add(db_post)
        self.db.commit()
        self.db.refresh(db_post)
        return db_post.id

    def get_posts(self, user_id: int) -> List[Post]:
        if user_id in post_cache:
            return post_cache[user_id]
        posts = self.db.query(Post).filter(Post.owner_id == user_id).all()
        post_cache[user_id] = posts
        return posts

    def delete_post(self, post_id: int, user_id: int):
        post = self.db.query(Post).filter(Post.id == post_id, Post.owner_id == user_id).first()
        if post is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Post not found"
            )
        self.db.delete(post)
        self.db.commit()
        post_cache.pop(user_id, None)
