import socket			 
s = socket.socket()	
host = socket.gethostname()	 
port = 5005			

s.connect((host, port)) 

f = open("Q16_1.txt","r")
msg = f.read();
s.send(msg.encode())
print('Server: ',s.recv(1024).decode())

s.close()
