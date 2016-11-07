import re
import socket
import sys
import time
from os import mkdir
import parse;


# def write_to_desk(file_name):
# 	with open("clientres/"+url, mode='wb+', buffering=BUFFER_SIZE) as file:
# 		with s:
# 			# FIXME: one byte then file is closed / while is infinity
# 			file.write(s.recv(BUFFER_SIZE));
# 			if s.recv(BUFFER_SIZE) == '':
# 				return;


def write_to_desk(file_name):
	with s:
		f=open("clientres/"+url, mode='wb+', buffering=BUFFER_SIZE);
		while 1:
			data =s.recv(BUFFER_SIZE)
			if data == b"":
				break
			f.write(data)


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


def get_req(url):
	byt = req_s % ("GET", url)
	byt = byt.encode()
	s.sendall(byt)

def post_req(url,file_name):
	s.sendall(req_s % ("POST",url));
	data=s.recv(BUFFER_SIZE)
	if data.upper()!='200 OK':
		return ConnectionError;
	with s:
		with open("clientres/"+file_name,mode='r',buffering=1024) as f:
			x = f.read()
			s.send(x.encode())




#setting defulats host and port num
#Default method = GET
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

#initiate connection

BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
s.connect((host,port))



#creating string using literals
req_s="%s /%s HTTP/1.0 "
data = req_s %(method.upper(),url) 

s.sendall(data.encode());

file_name = "image.jpeg"

rcvdata='';
# Main logic
if method.upper() == "GET":
	get_req(url)
	write_to_desk(url)
elif method.upper() =="POST":
	try:
		post_req(url,file_name)
	except ConnectionError as c_err:
		exit(c_err)
	



