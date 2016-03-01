import socket as request_library

my_socket = request_library.socket(request_library.AF_INET, request_library.SOCK_STREAM)
my_socket.connect(("www.py4inf.com", 80))

my_socket.send("GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n")

while True:
    data = my_socket.recv(512)
    if (len(data) < 1):
        break
    print data
my_socket.close()
