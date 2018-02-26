from json import dumps
import pika
from notifications.channels import BaseNotificationChannel


class BroadCastWebSocketChannel(BaseNotificationChannel):
    """Уведомление для RabbitMQ."""

    def _connect(self):
        """Connect RabbitMQ server."""
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost')
        )
        channel = connection.channel()

        return connection, channel

    def construct_message(self):
        """Создание сообщения"""
        extra_data = self.notification_kwargs['extra_data']

        return dumps(extra_data['message'])

    def notify(self, message):
        """Очередь RabbitMQ."""
        connection, channel = self._connect()

        uri = self.notification_kwargs['extra_data']['uri']

        channel.exchange_declare(exchange=uri, exchange_type='fanout')
        channel.basic_publish(exchange=uri, routing_key='', body=message)

        connection.close()
