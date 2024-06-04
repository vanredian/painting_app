from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import Dict, List


# Модели данных
#! Здесь
class RoomCreateRequest(BaseModel):
    name: str

class RoomJoinRequest(BaseModel):
    uid: UUID
    name: str

class Room(BaseModel):
    uid: UUID
    participants: List[str] = []
    
class User(BaseModel):
    id: int
    name: str
    email: str