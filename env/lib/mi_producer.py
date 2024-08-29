import pika
import json
import uuid

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='NuevaOrden')

    orden = {
        'orden_id': str(uuid.uuid4()), 
        'items': ['Hamburguesa Doble', 'Papas Especiales', 'Colombiana'],
        'total_orden': 40000.00  
    }

    # Convertir el pedido a formato JSON y enviar a la cola
    channel.basic_publish(
        exchange='',
        routing_key='NuevaOrden',
        body=json.dumps(orden)
    )

    print(f" [x] Orden #{orden['orden_id']} enviada a cola")

    # Cerrar la conexión
    connection.close()

if __name__ == '__main__':
    main()
