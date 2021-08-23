import socket
import yaml

ip = socket.gethostname()
port = 11234

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((ip, port))

print(f"Escutando {ip}: {port}")

def contains(hostname):
	stream = open("database.yaml", 'r')
	dictio = yaml.load(stream)
	if dictio is not None:
		if hostname in list(dictio.keys()):
			return True
	return False


def retrieve_database(hostname):
	if contains(hostname):
		stream = open("database.yaml", 'r')
		dictio = yaml.load(stream)
		response = dictio[hostname]
	else:
		response = f"{hostname} não existe neste servidor."
	return response

def register_database(record):
	hostname, ip = record[1:-1].split(',')
	if not contains(hostname):
		d = {hostname: ip}

		with open("database.yaml", 'w') as f:
			yaml.dump(d, f, default_flow_style=False)
		response = "Registro realizado com sucesso."
	else:
		response = "Registro já existe neste servidor."
	return response

while True:
	print('-'*50)

	data, addr = s.recvfrom(1024)
	print(data.decode("utf-8"))

	message = "Conexão com o servidor estabelecida.".encode("utf-8")
	s.sendto(message, addr)

	option, addr = s.recvfrom(1024)
	option = int(option.decode("utf-8"))

	if option == 1:
		hostname, addr = s.recvfrom(1024)
		response = retrieve_database(hostname.decode("utf-8"))
	elif option == 2:
		record, addr = s.recvfrom(1024)
		response = register_database(record.decode("utf-8"))

	s.sendto(response.encode("utf-8"), addr)	
