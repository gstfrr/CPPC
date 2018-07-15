import socket

HOST = '177.105.60.117'  # Symbolic name meaning all available interfaces
PORT = 22222  # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

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
