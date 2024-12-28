# LabTask1
## Подготовка:
1. Установить PostgreSQL.
2. В терминале, в корне проекта:
``` batch
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install poetry
poetry install
deactivate
```
3. Заменить в src/db.py переменную database_url под своего юзера, пароль и БД.
## Работа
### Начало работы
1. В терминале, в папке src:
``` batch
uvicorn main:app
```
2. Перейти в браузере по адресу http://127.0.0.1:8000/docs
### Прекращение работы:
1. В терминале нажать: 
<kbd>Ctrl</kbd> + <kbd>c</kbd>.  
2. Ввести:
``` batch
deactivate
```
