import socket

SEND_BUF_SIZE = 4096
RECV_BUF_SIZE = 4096

def update_buffer():
	sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
	# Get the size of the socket's send buffer
	bufsize = sck.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
	print "Intial Buffer size  :%d" %bufsize
	sck.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
	sck.setsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF,SEND_BUF_SIZE)
	sck.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,RECV_BUF_SIZE)
	bufsize = sck.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
	print "Updated Buffer size :%d" %bufsize

def block_modes():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setblocking(1)
	s.settimeout(0.5)
	s.bind(("127.0.0.1", 0))
	socket_address = s.getsockname()
	print "Trivial Server launched on socket: %s" %str(socket_address)
	#while(1):
		#s.listen(1)


update_buffer()
block_modes()
