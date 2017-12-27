import socket

import CreateJson
import netifaces as ni


def parse(string) -> str:
    s = string[6:string.find(" HTTP")]

    if len(s) > 1:
        string = s[1:]
        return string
    else:
        return "nothing"


createJson = CreateJson.CreateJson()
HOST, PORT = '', 8888
HOST_LOCAL = '127.0.0.1'  # ni.ifaddresses('lo0').get(2)[0].get('addr')
HOST_NETWORK = ni.ifaddresses('en0').get(2)[0].get('addr')

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST_LOCAL, PORT))
listen_socket.listen(1)

# print('Serving HTTP on port %s ...' % PORT)

print("address : " + HOST_LOCAL + ":" + str(PORT))
while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    r = parse(str(request))

    http_response = createJson.createDict

    client_connection.send(http_response.encode())
    client_connection.close()
