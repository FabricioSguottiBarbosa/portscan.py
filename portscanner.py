
import socket
host = input("IP address: ")
#ports = [1,22,23,25,53,80,111,135,139,443,445,3306,8080,9090] portas well-known
ports = range(1,1000)#porta 1 até 1000
for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#conecta o socket ao protocolo TCP
    client.settimeout(0.1)#Tempo de lâtencia
    code = client.connect_ex((host, port))#conecta o Ip retornando zero se a porta estiver aberta
    if code == 0:
        print(port, "open")