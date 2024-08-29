import pika
import json

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='NuevaOrden')

    def callback(ch, method, properties, body):
        orden = json.loads(body)
        print(f" [x] Procesando orden #{orden['orden_id']}")
        print(f"     Items: {orden['items']}")
        print(f"     Valor total: ${orden['total_orden']}")

    channel.basic_consume(
        queue='NuevaOrden',
        on_message_callback=callback,
        auto_ack=True
    )

    print(' [*] Esperando ordenes. Para salir presione CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    main()
