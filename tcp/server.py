import socket
import threading
import hangman

# hostname e porta
ip = socket.gethostname()
port = 11234


# cria objeto socket IPV4/TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((ip, port))

# escutar 5 conexões simultâneas
s.listen(5)

print(f"Listening {ip}: {port}")

def handle_client(client_socket):
	request = client_socket.recv(1024)
	request_decoded = request.decode("utf-8")
	print(f"Recebeu {request_decoded}")
	print(f"-------------------------")

	category, word = hangman.generate_word()
	word = word.lower()
	print(f"Palavra: {word}")
	hidden = "_"*len(word)
	
	client_socket.send(f"{category}".encode("utf-8"))
	client_socket.send(f"{hidden}".encode("utf-8"))


	while hidden.count('_') > 0:
		guess = client_socket.recv(1024).decode("utf-8").lower()
		if hangman.evaluate(word, hidden, guess):
			hidden = hangman.update(word, hidden, guess)

		client_socket.send(f"{hidden}".encode("utf-8"))

	client_socket.close()

# escutando para sempre
while True:
	client, address = s.accept()
	print(f"Connection from {address} has been established!")
	client_handler = threading.Thread(target=handle_client, args=(client,))
	client_handler.start()

