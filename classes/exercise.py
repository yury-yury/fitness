from pydantic import BaseModel, Field


class Exercise(BaseModel):
    name: str
    rep: str
    attempts: int = Field(le=10)
    weight: str
