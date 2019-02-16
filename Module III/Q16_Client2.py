import socket			 
s = socket.socket()	
host = socket.gethostname()	 
port = 5005				

s.connect((host, port)) 

f = open("Q16_2.txt","r")
msg = f.read();
s.send(msg.encode())
print('Sever: ',s.recv(1024).decode())

s.close()
