import os

print('List of network interfaces : ')
print(os.listdir('/sys/class/net/'))
