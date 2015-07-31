import socket


HOST = '127.0.0.1'
PORT = 10000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print (s.family)
print (s.type)
print (s.proto)
s.bind(('', PORT))
data,addr = s.recvfrom(1024)
print("Received {} from {}".format(repr(data), repr(addr)))
x = s.sendto(data, ('127.0.0.1',addr[1]))
print ("Send bytes", x)
s.close()
