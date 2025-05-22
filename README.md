# 🛡️ Registrace – Validátor s API (FastAPI)

Tento projekt ukazuje reálné testování a validaci uživatelské registrace pomocí Pythonu a FastAPI. Obsahuje:

✅ Validaci vstupů (jméno, heslo, email, datum narození, souhlas)  
✅ Automatizované testy pomocí `pytest`  
✅ REST API pomocí FastAPI  
✅ Interaktivní dokumentaci (Swagger UI)  
✅ Přípravu pro CI/CD

## 🚀 Spuštění

1. Nainstaluj závislosti:
```bash
pip install -r requirements.txt
Spusť server:

bash
Zkopírovat
Upravit
uvicorn main:app --reload
Otevři v prohlížeči:

arduino
Zkopírovat
Upravit
http://127.0.0.1:8000/docs
🧪 Testy
Spusť testy:

bash
Zkopírovat
Upravit
pytest
📦 Technologie
Python 3.10+

FastAPI

Uvicorn

Pytest

📌 Validované položky
Jméno (2–16 znaků, pouze písmena, pomlčky a apostrofy)

Heslo (min. 5 znaků, min. jedno velké písmeno a číslo)

Email (platný formát)

Datum narození (18+)

Souhlas s podmínkami