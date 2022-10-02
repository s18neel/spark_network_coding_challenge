from ast import Sub
from dataclasses import dataclass
import datetime
import enum
import pydantic


class State(str, enum.Enum):
    ACTIVE = "Active"
    REJECTED = "Rejected"
    INACTIVE = "Inactive"


class Message(pydantic.BaseModel):
    created_at: datetime.datetime = pydantic.Field(alias="createdAt")
    receiver_id: int = pydantic.Field(alias="receiverId")
    id: int
    sender_id: int = pydantic.Field(alias="senderId")


class Subscription(pydantic.BaseModel):
    created_at: datetime.datetime = pydantic.Field(alias="createdAt")
    start_date: datetime.datetime = pydantic.Field(alias="startDate")
    end_date: datetime.datetime = pydantic.Field(alias="endDate")
    status: State
    amount: float


class Profile(pydantic.BaseModel):
    gender: str | None
    is_smoking: bool = pydantic.Field(alias="isSmoking")
    profession: str
    income: float | None


class User(pydantic.BaseModel):
    id: int
    created_at: datetime.datetime = pydantic.Field(alias="createdAt")
    updated_at: datetime.datetime = pydantic.Field(alias="updatedAt")
    city: str | None
    country: str
    email: str
    profile: Profile
    subscription: list[Subscription]

    @property
    def email_domain(self) -> str:
        return self.email.split("@")[1]
