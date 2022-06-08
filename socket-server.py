import pymongo
import socket

# Bind the socket to the port
HOST = '172.27.0.2'                 
PORT = 8888
mBuffer = 1024
database_name = "sistemas_distribuidos"

URI = 'mongodb://172.27.0.1:27017'
client = pymongo.MongoClient(URI)
# print (client.list_database_names)
db = client[database_name]
collection = db['clientes']

# Insertar usuario
""" post = {'cedula': '1234567891', 'nombres': 'Diego'}
collection.insert_one(post).inserted_id """

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(3)

while True:
  print('Esperando conectar con un cliente')
  connection, client_address = sock.accept()
  try:
    print('Conectado desde', client_address)

    # Receive the data in small chunks and retransmit it
    while True:
      print('-------------------------------')
      data = connection.recv(mBuffer)
      print('Recibiendo dato: ' + format(data), "Typo:", type(data))

      cedula = data.decode('utf-8')
      if cedula == '':
        break
      obt = collection.find_one({'cedula': cedula})
      message = str(obt)
      print("output_byte", message)
      data = str.encode(message)

      if data:
        print('Enviando respuesta al cliente')
        connection.sendall(data)
      else:
        break

  except KeyboardInterrupt:
    break
  finally:
    connection.close()
