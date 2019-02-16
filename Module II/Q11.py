import socket

s = socket.socket()
host = socket.getfqdn()
port = 9081
s.bind((host, port))

print 'Starting server on', host, port
print 'The Web server URL for this would be http://%s:%d/' % (host, port)

s.listen(5)

print 'Entering infinite loop; Terminate manually to exit'

track = dict()

while True:
        c, (client_host, client_port) = s.accept()
        track[client_host] = track.get(client_host, 0) + 1
        c.recv(1000)
        c.send('HTTP/1.0 200 OK\n')
        c.send('Content-Type: text/html\n')
        c.send('\n')
        c.send("""
        <html>
        <body>
        <h1>Hello.</h1> Server Address : """+host+"""
        </body>
        </html>
        """)
        c.close()
        print 'Successfully Connected. '
