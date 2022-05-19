#### REST API для социальной cети yatube. Программный интерфейс предназначенный для управления сетью без применения web-браузера.
------
#### Как запустить проект:
* _Клонировать репозиторий и перейти в него в командной строке_:
```
git clone https://github.com/Dmitriy-kir/api_final_yatube.git
cd api_final_yatube
```
* _Cоздать и активировать виртуальное окружение_:
```
python -m venv venv
source venv/bin/activate
```
* _Установить зависимости из файла requirements.txt_:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
* _Для работы с JWT в Django установить и подключить две библиотеки Djoser и Simple JWT_:
```
pip install djoser djangorestframework-simplejwt==4.7.2
```
* _Выполнить миграции из дериктории yatube_api_:
```
python manage.py migrate
```
* _Запустить проект_:
```
python manage.py runserver
```
#### Документация доступна по ссылке:
```
http://127.0.0.1:8000/redoc/
```
#### Требования:
---
___Python 3.7 и выше___

___Django framework 2.2.16___

___Django Rest framework 3.12.4___

___Django Rest framework simplejwt 4.7.2___

___Pillow 8.3.1___

___PyJWT 2.1.0___

___requests 2.26.0___

___djoser 2.1.0___
