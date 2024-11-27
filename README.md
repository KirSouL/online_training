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

feature/task2 и feature/task3 и feature/task4
Для дальнейший работы над проектом необходимо произвести загрузку данных в БД.
В консоли написать команду: python manage.py loaddata online_training_data.json и 
python manage.py loaddata users/fixtures/payment_data.json, а также 
python manage.py loaddata users/fixtures/groups_data.json

feature/task4
Для просмотра покрытия тестами ввести в терминале: coverage report
