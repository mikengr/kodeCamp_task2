from pydantic import BaseModel, EmailStr
from datetime import date
from fastapi import FastAPI


app = FastAPI()


class Biodata(BaseModel):
    first_name: str
    middle_name: str = None
    last_name: str
    date_of_birth: date
    

class SignUpData(BaseModel):
    username: str
    email: EmailStr
    mobile_number: str
    password: str


@app.post("/sign_up/")
async def sign_up(user_info: Biodata, reg_info: SignUpData):
    return {
        "full_name": f"{f'{user_info.first_name} {user_info.middle_name} {user_info.last_name}'}"
                    if user_info.middle_name else f"{f'{user_info.first_name} {user_info.last_name}'}", 
        "date_of_birth": user_info.date_of_birth,
        "username": reg_info.username,
        "email": reg_info.email,
        "mobile": reg_info.mobile_number,
        "password": reg_info.password
    }
