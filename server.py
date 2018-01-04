import socket

import sys

import CreateJson
import netifaces as ni
import http.server

HOST, PORT = '', 8888
HOST_LOCAL = '127.0.0.1'  # ni.ifaddresses('lo0').get(2)[0].get('addr')
HOST_NETWORK = ni.ifaddresses('en0').get(2)[0].get('addr')


if __name__ == "__main__":
    createJson = CreateJson.CreateJson(net_adress=HOST_NETWORK+":"+str(PORT))

    handlerClass = http.server.BaseHTTPRequestHandler

    http.server.test(HandlerClass=http.server.SimpleHTTPRequestHandler, bind=HOST_NETWORK, port=PORT)

"""
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST_NETWORK, PORT))
listen_socket.listen(1)
"""
"""-----------------------------------------------------------------------"""

"""
print("address : " + HOST_NETWORK + ":" + str(PORT))
while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    r = parse(str(request))

    http_response = createJson.createDict

    client_connection.send(http_response.encode())
    client_connection.close()
"""