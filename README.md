### Для запуска:

1. Склонировать проект к себе на хост.
2. Открыть его через любую IDE.
3. Заменить данные в фале .env на свои (если необходимо).
4. В консоле ввести : docker compose -f docker-compose.yaml up
5. Прлижоение будет доступно по адресу localhost:8000/api/v1/login
6. В терминале Docker-образа приложения  ввести python ref_system/manage.py migrate, в ямле не захотели применяться миграции(сори).
7. Для тестов из корня приложения скопировать json фалы для Postman.
