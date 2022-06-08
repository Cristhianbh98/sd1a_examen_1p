import socket
import sys

HOST = '172.27.0.2'
PORT = 8888
mBuffer = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Conectado con el servidor en {}  port {}'.format(HOST,PORT))

sock.connect((HOST,PORT))

try:
	message = ''.join(sys.argv[1:]) or 'Default message'

	print('Enviando {!r}'.format(message))
	sock.sendall(str.encode(message))

	amount_received = 0
	amount_expected = len(message)
	print("Longitud de mensaje:", amount_expected)
	while amount_received < amount_expected:
		data = sock.recv(mBuffer)
		amount_received += len(data)
		print('received {!r}'.format(data))

finally:
	print('closing socket')
	sock.close()