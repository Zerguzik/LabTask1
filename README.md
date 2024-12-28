# LabTask1
## Подготовка:
1. Установить PostgreSQL.
2. Установить Python.
3. Установить зависимости, введя в терминале, в корне проекта:
``` batch
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install poetry
poetry install
deactivate
```
4. Заменить в src/db.py переменную database_url под своего юзера, пароль и БД.
## Работа
### Начало работы
1. Активировать виртуальное окружение в корне проекта, в терминале:
``` batch
.venv\Scripts\activate
```
2. Запустить приложение, написав в терминале, в папке src:
``` batch
uvicorn main:app
```
3. Перейти в браузере по адресу: http://127.0.0.1:8000/docs
### Прекращение работы:
1. В терминале приостановить работу приложения, нажав: 
<kbd>Ctrl</kbd> + <kbd>c</kbd>.  
2. Деактивировать виртуальное окружение, введя:
``` batch
deactivate
```
