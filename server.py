import socket



BUFFER_SIZE = 8  # 8 bit for fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 65432))
s.listen(1)

conn, addr = s.accept()
print('Connection address:', addr)
while 1:
   data = conn.recv(BUFFER_SIZE)
    if not data: break
    if data>=0 and data<=5:
   		speed = 51*data      #pulse width modulation. 255 for speed setting 5
   	if data == 'w'
   	print('[f'+ speed +'][f'+ speed +'][f'+ speed +'][f'+ speed + ']')
   	else if data == 's'
   	print('[r'+ speed +'][r'+ speed +'][r'+ speed +'][r'+ speed + ']')
   	else if data == 'a'
   	print('[r'+ speed +'][r'+ speed +'][f'+ speed +'][f'+ speed + ']')
   	else if data == 'd'
   	print('[f'+ speed +'][f'+ speed +'][r'+ speed +'][r'+ speed + ']')

conn.close()