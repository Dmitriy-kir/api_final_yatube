#### REST API для социальной cети yatube. Программный интерфейс предназначенный для управления сетью без применения web-браузера.
------
#### Как запустить проект:
* Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/Dmitriy-kir/api_final_yatube.git
cd api_final_yatube
```
* Cоздать и активировать виртуальное окружение:
```
python -m venv venv
source venv/bin/activate
```
* Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip setuptools
pip install -r requirements.txt
```
* Для работы с JWT в Django установить и подключить две библиотеки Djoser и Simple JWT:
```
pip install djoser djangorestframework-simplejwt==4.7.2
```
* Выполнить миграции из дериктории yatube_api:
```
python manage.py migrate
```
* Запустить проект:
```
python manage.py runserver
```
##### Документация доступна по ссылке:
```
http://127.0.0.1:8000/redoc/
```
##### Требования:
---
Python 3.7 и выше

Django framework 2.2.16

Django Rest framework 3.12.4

Django Rest framework simplejwt 4.7.2

Pillow 8.3.1

PyJWT 2.1.0

requests 2.26.0

djoser 2.1.0
