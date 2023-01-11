from typing import Optional
from uuid import UUID

from pydantic import BaseModel as PydanticSchema

from app.models import User


class UserSchema(PydanticSchema):

    id: Optional[UUID] = None
    email: str
    password: str

    def get_model(self) -> User:
        return User(
            id=self.id,
            email=self.email,
            password=self.password
        )

    @staticmethod
    def get_schema(user: User) -> 'UserSchema':
        return UserSchema(
            id=user.id,
            email=user.email,
            password=user.password
        )
