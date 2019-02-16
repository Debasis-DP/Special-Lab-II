import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_name = socket.gethostbyname('www.nitrkl.ac.in')
result = sock.connect_ex((sock_name,80))
if result == 0:
   print "Port is open"
else:
   print "Port is not open"
