import socket
from binascii import hexlify
def get_remote_machine_details():
	remote_host = "www.nitrkl.ac.in"
	ip_addr = socket.gethostbyname(remote_host)
	try:
		print "IP address of "+remote_host+" : "+ip_addr
		return ip_addr
	except socket.error, err_msg:
		print "%s: %s" %(remote_host, err_msg)

def convert_ip_addr(ip_addr):
	packed_ip_addr = socket.inet_aton(ip_addr)
	unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)
	print "IP Address: %s => Packed: %s, Unpacked: %s"\
	%(ip_addr, hexlify(packed_ip_addr), unpacked_ip_addr)
	
ip_addr = get_remote_machine_details()
convert_ip_addr(ip_addr)
