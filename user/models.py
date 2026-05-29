from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    username: str
    email: EmailStr | None = None
    full_name: str | None = None


class User(UserBase):
    disabled: bool | None = None
    roles: list[str] = Field(default_factory=list)


class UserInDB(UserBase):
    hashed_password: str


class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=20, pattern="^[a-zA-Z0-9_]+$")
    email: EmailStr
    full_name: str | None = Field(default=None, max_length=60)
    password: str = Field(min_length=6, max_length=50)
