from fastapi import FastAPI, Form
from validator import is_valid_registration

app = FastAPI()

@app.post("/register")
def register(
    name: str = Form(...),
    password: str = Form(...),
    email: str = Form(...),
    birthdate: str = Form(...),
    agreed: bool = Form(...)
):
    result = is_valid_registration(name, password, email, birthdate, agreed)
    if result is True:
        return {"success": True, "message": "Registrace proběhla úspěšně"}
    else:
        return {"success": False, "message": result[1]}
