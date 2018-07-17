import socket

HOST_SERVER = socket.getfqdn(socket.gethostbyname(socket.gethostname()))
# HOST = '177.105.60.133'  # The remote host
PORT = 22222  # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST_SERVER, PORT))

# mensagem para enviar
msg = 'Hello, bruno faz a porra do crc'

# enviar a mensagem
s.sendall(msg.encode())

# receber a resposta
data = s.recv(1024)
print('CLiente recebeu: ', repr(data))

s.close()
