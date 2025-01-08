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
Документацию можно изучить после запуска проекта по пути:
http://127.0.0.1:8000/redoc/ или http://127.0.0.1:8000/swagger/

Также подключена система оплаты онлайн курсов и уроков через Stripe.

feature/task6

Реализовано выполнение отложенных задач.

Для запуска обрабочика в консоли прописать:
1. Для UNIX систем celery -A config worker -l INFO
2. Для Windows celery -A config worker -l INFO -P eventlet

Для запуска периодической задачи в консоли прописать: 
celery -A config beat -l INFO

Для работы в Docker: docker-compose up -d --build
