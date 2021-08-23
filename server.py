import socket
import threading

# hostname e porta
ip = socket.gethostname()
port = 1234


# cria objeto socket IPV4/TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((ip, port))

# escutar 5 conexões simultâneas
s.listen(5)

print(f"Listening {ip}: {port}")

def handle_client(client_socket):
	request = client_socket.recv(1024)
	request_decoded = request.decode("utf-8")
	print(f"Received {request_decoded}")
	print(f"-------------------------")
	client_socket.send(bytes("Acknowledge!", "utf-8"))
	client_socket.close()

# escutando para sempre
while True:
	client, address = s.accept()
	print(f"Connection from {address} has been established!")
	client_handler = threading.Thread(target=handle_client, args=(client,))
	client_handler.start()