#### Список технологий: Python, Django Rest Framework, Docker, Gunicorn, Nginx, PostgreSQL,Pandas,Swagger


#### Задача:
    API: Сервис поиска ближайших машин для перевозки грузов.
## Установка
#### Шаг 1. Проверьте установлен ли у вас Docker
Прежде, чем приступать к работе, необходимо знать, что Docker установлен. Для этого достаточно ввести:
bash
docker -v
Или скачайте [Docker Desktop](https://www.docker.com/products/docker-desktop) для Mac или Windows. [Docker Compose](https://docs.docker.com/compose) будет установлен автоматически. В Linux убедитесь, что у вас установлена последняя версия [Compose](https://docs.docker.com/compose/install/). Также вы можете воспользоваться официальной [инструкцией](https://docs.docker.com/engine/install/).

#### Шаг 2. Клонируйте репозиторий себе на компьютер
Введите команду:
```bash
git clone https://github.com/Hovo-93/TruckLocator.git
```
#### Шаг 3. Создайте в клонированной директории файл .env
Пример:
```bash
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
DB_USER=admin
DB_PASSWORD=admin1234
DB_HOST=db
DB_PORT=5432
```

#### Шаг 4. Запуск docker-compose
Для запуска необходимо выполнить из директории с проектом команду:
```bash
docker-compose up -d
```
#### Документация
Документация к API доступна по адресу:
json
http://localhost:8080/swagger/

##### Другие команды
Создание суперпользователя:
```bash
    docker-compose exec web python manage.py createsuperuser
```
Для пересборки и запуска контейнеров воспользуйтесь командой:
```bash
    docker-compose up -d --build 
```
Останавливаем и удаляем контейнеры, сети, тома и образы:
```bash
Stop and Delete containers

docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)

Delete Images
docker rmi $(docker images -a -q)
```
## Примеры
Для формирования запросов и ответов использована программа [Postman](https://www.postman.com/).

### Получение списка грузов
```json
GET http://127.0.0.1:8000/api/cargo/list/
```
### Создание нового груза
```json
POST http://127.0.0.1:8000/cargo/create/


# Body(json)
{
    "pick_up_location": "99929",
    "delivery_location": "99926",
    "weight": 550,
    "description": "test"
}
```

### Получение информации о конкретном грузе по ID
```json
GET http://127.0.0.1:8000/cargo/detail/1/
```
### Редактирование груза по ID 
```json
PUT http://127.0.0.1:8000/cargo/update/1/

# Body(json)
{
    "weight": 435,
    "description": "test_update"
}
```
### Редактирование машины по ID
```json
PUT http://127.0.0.1:8000/truck/7528M/

# Body(json)
{
    "number": "3715W",
    "current_location": "624",
    "carrying": 49
}
```
### Удаление груза по ID
```json
DELETE http://127.0.0.1:8000/cargo/delete/1/

# Body(json)
{
   "id":1   
}
```        
### Получение машины по ID
```json
GET http://127.0.0.1:8000/truck/7528M/
```


