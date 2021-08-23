import socket

ip = socket.gethostname()
port = 11234

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = "Solicitando serviço de tradução de endereços DNS.".encode("utf-8")
s.sendto(message, (ip, port))

data, addr = s.recvfrom(1024)
print(data.decode("utf-8"))

print("Selecione uma opção:")
print("1 - Consulta DNS")
print("2 - Registro DNS")

option = input().encode("utf-8")
s.sendto(option, (ip, port))

if int(option) == 1:
	print("Insira o hostname: ", end='')
	hostname = input().encode("utf-8")
	s.sendto(hostname, (ip, port))
elif int(option) == 2:
	print("Insira o registro: ", end='')
	record = input().encode("utf-8")
	s.sendto(record, (ip, port))

response, addr = s.recvfrom(1024)
print(response.decode("utf-8"))