from pydantic import BaseModel

class User(BaseModel):
    """The author of a tweet"""
    name: str
    """The name of the user"""
    username: str
    """The username of the user"""