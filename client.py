import socket

# hostname e porta
ip = socket.gethostname()
port = 11234

# cria objeto socket IPV4/TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((ip, port))

# mensagem de requisição
s.send("Solicitação de novo jogo.".encode("utf-8"))

category = s.recv(1024).decode("utf-8")
hidden = s.recv(1024).decode("utf-8")

print("Categoria: " + category)
print("Palavra: " + ' '.join(list(hidden)))

while hidden.count('_') > 0:
	guess = input("Insira a letra ou palavra: ")
	s.send(guess.encode("utf-8"))
	
	hidden = s.recv(1024).decode("utf-8")

	print("Palavra: " + ' '.join(list(hidden)))