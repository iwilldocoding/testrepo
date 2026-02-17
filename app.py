from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field, field_validator
from typing import Annotated

app = FastAPI()


class UserSignup(BaseModel):
    name: str = Field(min_length=2,pattern=r"^[a-zA-Z\s]+$")
    age: int = Field(ge=0) 
    @field_validator('age')
    @classmethod
    def check_age(cls, v: int):
        if v < 18:
            raise ValueError('You must be at least 18 years old to register.')
        return v
    @field_validator('name')
    @classmethod
    def check_name(cls,n:str):
        if n(" ","").isalpha():
            raise ValueError('Name must only contain letters')
        return n

@app.get("/", response_class=HTMLResponse)
async def get_form():
    return """
    <html>
        <body style="font-family: sans-serif; display: flex; justify-content: center; padding: 50px;">
            <form action="/verify" method="post" style="display: flex; flex-direction: column; gap: 10px; width: 300px;">
                <h2>Register</h2>
                <input type="text" name="name" placeholder="Full Name" required>
                <input type="number" name="age" placeholder="Age" required>
                <button type="submit" style="background: #007bff; color: white; border: none; padding: 10px; cursor: pointer;">Verify Me</button>
            </form>
        </body>
    </html>
    """

@app.post("/verify")
async def verify_user(
    name: Annotated[str, Form()], 
    age: Annotated[int, Form()]
):
    try:

        user = UserSignup(name=name, age=age)
        return {"status": "Success", "message": f"Welcome, {user.name}!"}
    except Exception as e:
        return {"status": "Error", "detail": str(e)}
#hello this is the master branch
