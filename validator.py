import re
from datetime import datetime
from typing import Union

def is_valid_name(name: str) -> Union[bool, tuple[bool, str]]:
    if not (2 <= len(name) <= 16):
        return False, "Jméno musí mít 2 až 16 znaků"
    if not re.fullmatch(r"[A-Za-zÁČĎÉĚÍŇÓŘŠŤÚŮÝŽáčďéěíňóřšťúůýž\-']+", name):
        return False, "Jméno může obsahovat jen písmena, pomlčky a apostrofy"
    return True

def is_valid_password(password: str) -> Union[bool, tuple[bool, str]]:
    if len(password) < 5:
        return False, "Heslo musí mít alespoň 5 znaků"
    if not re.search(r'[A-Z]', password):
        return False, "Heslo musí obsahovat alespoň jedno velké písmeno"
    if not re.search(r'\d', password):
        return False, "Heslo musí obsahovat alespoň jedno číslo"
    return True

def is_valid_email(email: str) -> Union[bool, tuple[bool, str]]:
    if not re.fullmatch(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
        return False, "Neplatný formát emailu"
    return True

def is_valid_birthdate(birthdate: datetime) -> bool:
    today = datetime.now()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age >= 18

def parse_birthdate(date_str: str) -> Union[datetime, None]:
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return None

def is_valid_registration(name: str, password: str, email: str, birthdate_str: str, agreed: bool) -> Union[bool, tuple[bool, str]]:
    name_check = is_valid_name(name)
    if name_check is not True:
        return name_check

    password_check = is_valid_password(password)
    if password_check is not True:
        return password_check

    email_check = is_valid_email(email)
    if email_check is not True:
        return email_check

    birthdate = parse_birthdate(birthdate_str)
    if not birthdate:
        return False, "Neplatný formát data narození (očekává se YYYY-MM-DD)"

    if not is_valid_birthdate(birthdate):
        return False, "Musí vám být alespoň 18 let"

    if not agreed:
        return False, "Musíte souhlasit s podmínkami"

    return True
