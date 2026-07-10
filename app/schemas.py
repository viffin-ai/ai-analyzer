from pydantic import BaseModel

class RequestData(BaseModel):
    text: str
    user_id: int

    