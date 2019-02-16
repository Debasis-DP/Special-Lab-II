import socket
import struct
import sys
import time
import ntplib
from time import ctime



def get_time():
	c = ntplib.NTPClient()
	response = c.request('pool.ntp.org')
	print(ctime(response.tx_time))


def sntp_client():
	NTP_SERVER = "0.uk.pool.ntp.org"
	TIME1970 = 2208988800L 
	client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	data = '\x1b' + 47 * '\0'
	client.sendto(data, (NTP_SERVER, 123))
	data, address = client.recvfrom( 1024 )
	if data:
		print 'Response received from:', address
	t = struct.unpack( '!12I', data )[10]
	t -= TIME1970
	print '\tTime=%s' % time.ctime(t)

sntp_client()
get_time()
