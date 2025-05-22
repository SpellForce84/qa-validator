from validator import is_valid_name, is_valid_password, is_valid_registration, is_valid_email
from datetime import datetime

# === TESTY JMÉNA ===
def test_valid_name():
    assert is_valid_name("Jan") == True
    assert is_valid_name("Éva") == True
    assert is_valid_name("O'Reilly") == True
    assert is_valid_name("Jean-Luc") == True
    assert is_valid_name("A") == (False, "Jméno musí mít 2 až 16 znaků")
    assert is_valid_name("J" * 17) == (False, "Jméno musí mít 2 až 16 znaků")
    assert is_valid_name("John123") == (False, "Jméno může obsahovat jen písmena, pomlčky a apostrofy")
    assert is_valid_name("Anna@Home") == (False, "Jméno může obsahovat jen písmena, pomlčky a apostrofy")

# === TESTY HESLA ===
def test_valid_password():
    assert is_valid_password("Hello1") == True
    assert is_valid_password("abc1") == (False, "Heslo musí mít alespoň 5 znaků")
    assert is_valid_password("abcde") == (False, "Heslo musí obsahovat alespoň jedno velké písmeno")
    assert is_valid_password("ABCDE") == (False, "Heslo musí obsahovat alespoň jedno číslo")

# === TESTY EMAILU ===
def test_valid_email():
    assert is_valid_email("user@example.com") == True
    assert is_valid_email("userexample.com") == (False, "Neplatný formát emailu")
    assert is_valid_email("user@com") == (False, "Neplatný formát emailu")

# === TESTY REGISTRACE ===
def test_valid_registration():
    assert is_valid_registration("Jan", "Abcd1", "jan@example.com", "2000-01-01", True) == True
    assert is_valid_registration("Jan", "Abcd1", "jan@example.com", "2010-01-01", True) == (False, "Musí vám být alespoň 18 let")
    assert is_valid_registration("Jan", "Abcd1", "janexample.com", "2000-01-01", True) == (False, "Neplatný formát emailu")
    assert is_valid_registration("Jan", "abcd1", "jan@example.com", "2000-01-01", True) == (False, "Heslo musí obsahovat alespoň jedno velké písmeno")
    assert is_valid_registration("John123", "Abcd1", "jan@example.com", "2000-01-01", True) == (False, "Jméno může obsahovat jen písmena, pomlčky a apostrofy")
    assert is_valid_registration("Jan", "Abcd1", "jan@example.com", "2000-01-01", False) == (False, "Musíte souhlasit s podmínkami")
    assert is_valid_registration("Jan", "Abcd1", "jan@example.com", "neco", True) == (False, "Neplatný formát data narození (očekává se YYYY-MM-DD)")
