## Приложение на Django для работы с базой книг

#### Как развернуть
Склонируйте репозиторий и создайте виртуальное окружение:
```
git clone https://github.com/charlieplanka/skillfactory-D4-django-library.git
virtualenv library
```
Активируйте окружение и установите зависимости:
```
cd library
./Scripts/activate
pip install -r requirements.txt
```

Запуск (по умолчанию сервер поднимется на 8000 порту):

```
cd my_site
python manage.py runserver
```

На главной странице расположена таблица со всеми книгами, которые есть в базе.  
В каждой строке есть кнопки «Увеличить кол-во» и «Уменьшить кол-во», которые увеличивают или уменьшают количество экземпляров книги.  

![Books](/preview_images/lib.png)
  
По пути **/publishers** отображается список всех издательств, которые есть в базе.  
По пути **/borrowed_books** отображается список всех книг, которые одолжили друзья.  

![Friends](/preview_images/friends.png)

### Админка
Для создания пользователя с правами администратора выполните комнаду:
```
python manage.py createsuperuser
```

В админке **/admin** доступны списки книг, авторов, издательств и друзей.  
Каждую книгу можно связать с автором, издательством (необязательное поле) и другом (необязательное поле), который её одолжил. На странице каждого издательства отображаются связанные книги, на странице друга — книги, которые он одолжил.
