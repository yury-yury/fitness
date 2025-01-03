from pydantic import BaseModel


class Exercise(BaseModel):
    name: str
    rep: str
    attempts: int
    wedth: str
