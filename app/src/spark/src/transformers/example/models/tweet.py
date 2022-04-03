from pydantic import BaseModel
from typing import List
import datetime
from user import User

class Tweet(BaseModel):
    """All the details of a Tweet"""
    text: str
    """The content of a tweet"""
    author: User
    """The author of a tweet"""
    reply_to: List[User] = None
    """The list of users it replies to, it may be None"""
    creation_date: datetime.datetime
    """The date the tweet was created"""