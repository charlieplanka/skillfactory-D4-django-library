## Приложение на Django для работы с базой книг

Перед запуском приложения установите зависимости!
```
pip install -r requirements.txt
```

Запуск (по умолчанию сервер поднимется на 8000 порту):

```
cd my_site
python manage.py runserver
```

На главной странице расположена таблица со всеми книгами, которые есть в базе.  
В каждой строке есть кнопки «Увеличить кол-во» и «Уменьшить кол-во», которые увеличивают или уменьшают количество экземпляров книги.  
  
По пути **/publishers** отображается список всех издательств, которые есть в базе.  
По пути **/borrowed-books** отображается список всех книг, которые одолжили друзья.  

### Админка
Для создания пользователя с правами администратора выполните комнаду:
```
python manage.py createsuperuser
```

В админке **/admin** доступны списки книг, авторов, издательств и друзей.  
Каждую книгу можно связать с автором, издательством (необязательное поле) и другом (необязательное поле), который её одолжил. На странице каждого издательства отображаются связанные книги, на странице друга — одолженные книги.
