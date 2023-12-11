# 🧑‍💻 Онлайн приложение `Book catalog` для поиска и оценки книг.

### Содержание:
  - [1. Краткое описание приложения](#short_description)
  - [2. Старт работы (как запустить приложение)](#start)
  - [3. 🌍 Пароли и логины для входа ](#login)
  - [4. 📝 Функционал `пользователя`](#functional_applicant)
  - [5. 📝 Использование `API`](#api_usage)


---
<a id='short_description'></a>
## 1. Краткое описание приложения

Приложение `HeadHunter` - платформа `по поиску работы и сотрудников`, позволяющая работодателям быстро выбрать подходящих работников, а соискателям – искомую работу.

 ---
<a id='start'></a>
## 2. Старт работы (как запустить приложение)

Чтобы запустить `приложение` локально, необходимо произвести `клонирование` себе на устройство следующей командой

```python
   $ git clone https://github.com/ValentinKim531/book_catalog.git
```

После успешного клонирования проекта, создаем и активируем `виртуальное окружение` 
```python
   $ python3 -m virtualenv venv
```
```python
   $ source venv/bin/activate 
```
и загружаем все зависимости проекта:

```python
   pip3 install -r requirements.txt
```

Затем необходимо создать `базу PostgresQL` и внести соответствующие настройки в `settings.py` в ядре проекта:

```python
   DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "[название созданной базы]",
        "USER": "[имя юзера базы]",
        "PASSWORD": "[пароль юзера базы]",
        "HOST": "localhost",
        "PORT": "",
    }
}
```

Далее применяем `миграции` командой:

```python
   python manage.py migrate
```

`Запуск` проекта командой:

```python
   python manage.py runserver
```

Для закрузки `фикстур` проекта используем команду:

```python
   pythin manage.py loaddata ./fixtures/fixtures.json  
```
---

---
<a id='login'></a>
## 3. 🌍 Пароли и логины для входа и тестирования приложения


<table>
    <tr>
        <th>Вход для:</th>
        <th>Логин</th>
        <th>Пароль</th>
    </tr>
    <tr>
        <td>администратора(admin)</td>
        <td>admin@admin.com</td>
        <td>admin</td>
    </tr>
    <tr>
        <td>соискателя (applicant)</td>
        <td>user@user.com</td>
        <td>user</td>
    </tr>
</table>


---
<a id='functional_applicant'></a>
## 4. 📝 Функционал `пользователя`

**Контент создается через Django admin:**

```python
   http://127.0.0.1:8000/admin
```

**Пользователь может:**
* Осуществлять фильтрацию (поиск) книг по автору, жанру, дате публикации книги
* Выставлять рейтинг книги (от 1 до 5)
* Просматривать детали описания каждой книги, отзывы и средний рейтинг пользователей 
* Добавлять книги в избранное
* Управлять собственным профилем (регистрация, смена пароля, редактирование профиля)


---
<a id='api_usage'></a>
## 5. 🌐 Использование API

API приложения `Book catalog` позволяет взаимодействовать с данными о книгах, авторах, жанрах, отзывах и пользователях. Ниже представлены основные эндпоинты API:

### Эндпоинты:

- `GET /api/books/` - получить список всех книг.
- `POST /api/books/` - добавить новую книгу (требуется аутентификация).
- `GET /api/books/{id}/` - получить детальную информацию о книге.
- `PUT /api/books/{id}/` - обновить информацию о книге (требуется аутентификация).
- `DELETE /api/books/{id}/` - удалить книгу (требуется аутентификация).

- `GET /api/authors/` - получить список всех авторов.
- `POST /api/authors/` - добавить нового автора (требуется аутентификация).

- `GET /api/genres/` - получить список всех жанров.
- `POST /api/genres/` - добавить новый жанр (требуется аутентификация).

- `GET /api/reviews/` - получить список всех отзывов.
- `POST /api/reviews/` - добавить новый отзыв (требуется аутентификация).

- `POST /api/accounts/` - регистрация нового пользователя.
- `POST /api/accounts/login/` - аутентификация пользователя.

### Документация API:

Для более подробной информации о API, включая параметры запросов и форматы ответов, посетите:

```python
   http://127.0.0.1:8000/swagger/
```



