##HTTP 1.1 client
import socket
import sys
import time

import parse


def get_req(url):
	byt = req_s % ("GET", url)
	byt = byt.encode()
	s.sendall(byt)

def write_to_desk(file_name):
		f=open("clientres/"+url, mode='wb+', buffering=BUFFER_SIZE);
		while 1:
			data =s.recv(BUFFER_SIZE)
			if data == b"":
				return
			f.write(data)

#TODO test the travering
def traverse(file_name):
	#TODO parse file's contents send gets till complete
	# TODO: recursiion or not recursion
	url=[];
	if file_name.endswith('.txt'):
		# with open("clientres/"+file_name,'w+') as file:
			x = file_name.readlines();
			for l in x:
				parsed=parse.req(l);
				url.append(( parsed['method'], parsed['url'] ))


def post_req(url):
	byt = req_s % ("POST",url)
	byt = byt.encode()
	s.sendall(byt)
	data = s.recv(BUFFER_SIZE)

	if data.upper()!=b'200 OK':
		return ConnectionError;
	with s:
		try:
			with open("clientres/"+url, mode='rb',buffering=1024) as f:
				 s.send(f.read())
		except FileNotFoundError as err:
			s.sendall(b'404 NOT FOUND')
			print(err)
			return

try:
	method = sys.argv[1] 
except IndexError as err:
	method = "GET"

#Default url to get
try:
	url= sys.argv[2]
except IndexError as err:
	url="index.html"

try:
	host=sys.argv[3];
except IndexError as err:
	host='localhost';

try:
	port=sys.argv[4];
except IndexError as s:
	port=5007;

BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
s.connect((host,port))

##############################TESTING##########
print("Connected")
s.settimeout(4)



x = s.recv(BUFFER_SIZE)
print(x, time.clock())

while True:
	y=1

print(x)
###############################
#creating string using literals
req_s="%s /%s HTTP/1.0 "
data = req_s %(method.upper(),url) 

# s.sendall(data.encode());

rcvdata='';

# # Main logic
# if method.upper() == "GET":
# 	get_req(url)
# 	write_to_desk(url)
# elif method.upper() =="POST":
# 	try:
# 		post_req(url)
# 	except ConnectionError as c_err:
# 		exit(c_err)
