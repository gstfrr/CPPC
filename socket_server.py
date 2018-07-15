import socket

HOST_SERVER = socket.getfqdn(socket.gethostbyname(socket.gethostname()))
PORT = 45454  # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST_SERVER, PORT))
s.listen(1)

print('Servidor ', HOST_SERVER, ' escutando na porta ', PORT)

#recebe mensagem
while 1:
    # recebe conexao
    conn, addr = s.accept()
    print('Connected by', addr)
    data = conn.recv(1024)
    if not data:
        #break
        continue
    print('servidor recebeu',repr(data))

    #responde
    conn.sendall("valeu".encode())

conn.close()
