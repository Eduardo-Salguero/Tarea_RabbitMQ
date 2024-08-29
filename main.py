import sys
import env.lib.mi_producer as producer
import env.lib.mi_consumer as consumer

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Uso: python main.py [producer|consumer]")
        sys.exit(1)

    role = sys.argv[1]

    if role == 'producer':
        producer.main()
    elif role == 'consumer':
        consumer.main()
    else:
        print("Argumento inválido. Usa 'producer' o 'consumer'.")
        sys.exit(1)
