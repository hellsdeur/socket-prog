import socket

# hostname e porta
ip = socket.gethostname()
port = 1234

# cria objeto socket IPV4/TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((ip, port))

# mensagem de requisição
s.send(bytes("Request message lol", "utf-8"))

msg = s.recv(1024)
print(msg.decode("utf-8"))