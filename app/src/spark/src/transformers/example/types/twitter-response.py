from pydantic import BaseModel
from typing import List
from tweet import Tweet

class TwitterResponse(BaseModel):
    """The response from the Twitter API"""
    tweets: List[Tweet]
    """All the tweets it retrieved"""