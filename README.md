# WomsChat

Чат в реальном времени

Vue, Django, RabbitMQ and uWSGI WebSockets.

## Установка

### Vue

Перейти в  `WomsChat`:

```bash
cd WomsChat
```

Установить, выполнив:

``` bash
npm install
```

Запустить сервер (localhost:8080):

```bash
npm run dev
```

### Django

Установить зависимости, выполнив

```bash
pip install -r requirements.txt
```

Запустить сервер (localhost:8000):

```bash
python manage.py runserver
```

### RabbitMQ

Для чата используется RabbitMQ и uWSGI WebSocket сервер. Установить
(https://www.rabbitmq.com/download.html).

### WebSocket сервер
Старт

```bash
uwsgi --http :5000 --gevent 100 --module websocket --gevent-monkey-patch
--master
```
