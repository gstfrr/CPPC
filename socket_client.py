import socket

HOST = '127.0.0.1'  # The remote host
PORT = 22222  # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# mensagem para enviar
msg = 'Hello, world'

#enviar a mensagem
s.sendall(msg.encode())

#receber a resposta
data = s.recv(1024)
print('CLiente recebeu: ', repr(data))

s.close()

