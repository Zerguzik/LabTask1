from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    login: str
    password: str


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    login: str = Field(index=True)


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    login: str | None
    password: str | None


class UserPublic(UserBase):
    id: int
