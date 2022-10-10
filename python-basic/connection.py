import socket

mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(("www.google.com",80))
cmd = 'www.instagram.com'.encode()
mysock.send(cmd)
