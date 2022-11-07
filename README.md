# Менеджер учёта расходов | [SQL Задачи](https://github.com/smnenko/outlays_manager/tree/master/sql_tasks)

### Список реализованного:
1. Регистрация, авторизация, профиль
2. Категории CRUD
3. Транзакции CRUD
4. Отправка статистики
5. Docker и Docker Compose

### Краткое овервью:
1. Токен получал при помощи _djangorestframework-simplejwt_
2. Транзации (_Transaction_) изменяют баланс пользовательского счёта (_Account_) на уровне ORM через переопределение методов _save_ и _delete_ у модели и метода 
_delete_ у **TransactonQuerySet**, чтобы баланс изменялся как при взаимодействии с _django-admin_, так и с _API_-запросами.
4. Статистику отправляю при помощи Django + Celery + Redis: [сбор](https://github.com/smnenko/outlays_manager/blob/master/outlays_manager/apps/account/utils.py)
и [отправка](https://github.com/smnenko/outlays_manager/blob/master/outlays_manager/apps/core/tasks.py)

### Стек проекта:
- python 3.10
- django 4.1.3
- djangorestframework 3.14.0
- celery 5.2.7
