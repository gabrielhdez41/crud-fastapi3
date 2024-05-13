from pydantic import BaseModel  # type: ignore

class Todo(BaseModel):
    name: str
    description: str
    complete: bool