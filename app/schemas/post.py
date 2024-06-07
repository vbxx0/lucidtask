from pydantic import BaseModel, constr


class PostCreate(BaseModel):
    text: constr(max_length=5 * 1024 * 1024)


class PostResponse(BaseModel):
    id: int
    text: str

    class Config:
        orm_mode = True
