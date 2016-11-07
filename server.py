import os
import re
import socket
import time

import parse
from concurrent.futures import ThreadPoolExecutor

#  TODO: generate a proper http response;
#  TODO: serving files and closing the connections.
### HTTP 1.1

HOST = ''
PORT = 5007

BUFFER_SIZE = 1024
SERVER_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER_SOCKET.bind((HOST, PORT))

def serve_master(conn):
	with conn:
		#TODO async polling till timeout
		data = conn.recv(BUFFER_SIZE)
		p = parse.req(data.decode())
		print(p['method'], p['url'])
		
		if p['method'] == "GET":
			serve_get(conn, p['url'])
		elif p['method'] == "POST":
			
			conn.sendall(b"200 OK")
			serve_post(conn, p['url'])

def serve_get(conn, url):
	try:
		with open("res"+url, mode='rb', buffering=BUFFER_SIZE) as f:
			conn.send(f.read())
	except FileNotFoundError as err:
		conn.sendall(b'404 NOT FOUND')
		print(err)
		return

def serve_post(conn, url):
	with conn:
		f = open("res"+url, mode='wb+', buffering=BUFFER_SIZE)
		while 1 :
			data = conn.recv(BUFFER_SIZE)
			if data == b"":
				break
			f.write(data)

def welcoming_thread():
	while 1:
		SERVER_SOCKET.listen(3)
		CONN, ADDR = SERVER_SOCKET.accept()
		CONN.settimeout(2)
		executors.submit(serve_master, CONN)

executors = ThreadPoolExecutor(max_workers=3)
