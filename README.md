## Приложение на Django для работы с базой книг

### Структура приложения

В шапке сайта есть навигация для переключения между страницами.
##### Библиотека

Вся информация по книгам, которые есть в базе.  
Можно увеличить или уменьшить количество экзмепляров книги с помощью кнопок «+» и «-».

##### Авторы

Список всех авторов, которые есть в базе.

##### Издательства

Список всех издательств, которые есть в базе.

##### Книги у друзей

Список всех книг, которые одолжили друзья.  

##### Добавить книгу

Можно добавить новую книгу в библиотеку. Обязательные поля помечены звёздочками.  
После добавления открывается страница со списком книг.

##### Добавить автора

Можно добавить автора в библиотеку. Обязательные поля помечены звёздочками.  
После добавления открывается страница со списком авторов.

### Админка
Для создания пользователя с правами администратора выполните комнаду:
```
python manage.py createsuperuser
```

В админке **/admin** доступны списки книг, авторов, издательств и друзей.  
Можно как добавлять новые записи, так и редактировать существующие.  
  
Например, чтобы изменить параметры книги:
1. Откройте страницу админки (по умолчанию — http://127.0.0.1:8000/admin/).
2. Залогиньтесь под админом (команда создания администратора выше).
3. Откройте страницу с книгами.  
![](https://i.imgur.com/Ah72Ktu.png)
4. Выберите нужную книгу.  
![](https://i.imgur.com/okPRdAF.png)
5. Внесите изменения в нужные поля.
6. Сохраните изменения, нажав на кнопку Save в правом нижнем углу.  
![](https://i.imgur.com/4vyS5va.png)

Кнопка для добавления новых записей находится в верхнем правом углу на странице каждого раздела.  
 
![](https://i.imgur.com/0VCnfoH.png)

Новые книги и новых авторов можно добавлять и через интерфейс приложения (см. структуру выше).
  
Каждую книгу можно связать с автором, издательством (необязательное поле) и другом (необязательное поле), который её одолжил. На странице каждого издательства отображаются связанные книги, на странице друга — книги, которые он одолжил.

### Как развернуть 
#### Windows
1. Склонируйте репозиторий и создайте внутри папки виртуальное окружение:
```
git clone https://github.com/charlieplanka/skillfactory-D4-django-library.git
cd skillfactory-D4-django-library
virtualenv library
```
2. Активируйте окружение и установите зависимости:
```
.\library\Scripts\activate
pip install -r requirements.txt
```
3. Сгенерируйте секретный ключ на [Djecrety](https://djecrety.ir/).
4. Создайте файл .env рядом с файлом settings.py и запишите в него значение ключа (без кавычек и пробелов):
```
Echo 'SECRET_KEY=0#*rrb+!hpo_e=bt(5w=e3(r=yige=)z$-7eccj*3z$0#4zoec' > ".\my_site\my_site\.env"
```
5. Вернитесь на уровень выше (в папку с файлом manage.py) и запустите сервер (по умолчанию поднимется на 8000 порту):
```
cd ..
python manage.py runserver
```

#### Linux
1. Склонируйте репозиторий и создайте внутри папки виртуальное окружение:
```
git clone https://github.com/charlieplanka/skillfactory-D4-django-library.git
cd skillfactory-D4-django-library
python3 -m venv library
```
2. Активируйте окружение и установите зависимости:
```
source library/bin/activate
pip install -r requirements.txt
```
3. Сгенерируйте секретный ключ на [Djecrety](https://djecrety.ir/).
4. Создайте файл .env рядом с файлом settings.py и запишите в него значение ключа (без кавычек и пробелов):
```
echo 'SECRET_KEY=0#*rrb+!hpo_e=bt(5w=e3(r=yige=)z$-7eccj*3z$0#4zoec' > my_site\my_site\.env
```
5. Перейдите в папку с приложением и запустите сервер (по умолчанию поднимется на 8000 порту):
```
cd .\my_site\
python manage.py runserver
```
