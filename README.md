Перед работай с проектом рекомендовано произвести настройки в PostgreSQL сервере,
а именно в файле pg_hba.conf настроить параметры аутентификации для сервера своей
машины. Согласно примеру ниже.

# TYPE  DATABASE        USER            ADDRESS                 METHOD

# "local" is for Unix domain socket connections only
local   all             all                                     trust
# IPv4 local connections:
host    all             all             127.0.0.1/32            trust
# IPv6 local connections:
host    all             all             ::1/128                 trust
# Allow replication connections from localhost, by a user with the
# replication privilege.
local   replication     all                                     trust
host    replication     all             127.0.0.1/32            trust
host    replication     all             ::1/128                 trust

После настройки подключения к базе данных локального сервера ввод пароля не требуется.

Для работы с проектом необходимо дополнительно создать базу данных в Postgresql
и указать её в файле .env.sample, далее необходимо сохранить файл .env.sample как .env

feature/task2 и feature/task3, и feature/task4, и feature/task5
Для дальнейший работы над проектом необходимо произвести загрузку данных в БД.
В консоли написать команду: python manage.py loaddata online_training_data.json и 
python manage.py loaddata users/fixtures/payment_data.json, а также 
python manage.py loaddata users/fixtures/groups_data.json

feature/task4
Для просмотра покрытия тестами ввести в терминале: coverage report


feature/task5
В проекте подключена библиотека для автоматической генерации документации.
Документацию можно изучить после запуска проекта по пути: http://127.0.0.1:8000/redoc/ или http://127.0.0.1:8000/swagger/

Также подключена система оплаты онлайн курсов и уроков через Stripe.

feature/task6

Реализовано выполнение отложенных задач.

Для запуска обрабочика в консоли прописать:
1. Для UNIX систем celery -A config worker -l INFO
2. Для Windows celery -A config worker -l INFO -P eventlet

Для запуска периодической задачи в консоли прописать: 
celery -A config beat -l INFO
