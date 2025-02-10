from pydantic import BaseModel, Field


class Exercise(BaseModel):
    name: str
    rep: int
    attempts: int = Field(le=10)
    weight: float
