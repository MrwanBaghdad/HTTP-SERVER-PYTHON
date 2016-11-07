import os
import re
import socket
import time

import parse
from concurrent.futures import ThreadPoolExecutor

HOST = ''
PORT = 5007


BUFFER_SIZE = 1024
SERVER_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER_SOCKET.bind((HOST, PORT))

def serve_get(conn, url):
	with conn:
		try:
			with open("res"+url, mode='rb', buffering=BUFFER_SIZE) as f:
				conn.send(f.read())
		except FileNotFoundError as err:
			conn.sendall(b'404 NOT FOUND')
			print(err)
			return


# def serve_post(conn, url):
# 	with conn:
# 		with open(url, mode='wb+', buffering=BUFFER_SIZE) as f:
# 			data = conn.recv(BUFFER_SIZE)
# 			f.write(data)

def serve_post(conn, url):
	with conn:
		f = open("res"+url, mode='wb+', buffering=BUFFER_SIZE)
		while 1 :
			data = conn.recv(BUFFER_SIZE)
			if data == b"":
				break
			f.write(data)

def serve_master(conn):
	data = conn.recv(BUFFER_SIZE)
	p = parse.req(data.decode())
	if p['method'] == "GET":
		serve_get(conn, p['url'])
	elif p['method'] == "POST":
		conn.sendall(b"200 OK")
		serve_post(conn, p['url'])


def welcoming_thread():
	while 1:
		SERVER_SOCKET.listen(3)
		CONN, ADDR = SERVER_SOCKET.accept()
		executors.submit(serve_master, CONN)

#TODO: threading
executors = ThreadPoolExecutor(max_workers=3)

while 1:
	SERVER_SOCKET.listen(1)
	CONN, ADDR = SERVER_SOCKET.accept()
	with CONN:
		print('connected by ', ADDR)
		while True:
			# data = CONN.recv(BUFFER_SIZE)
			# # CONN.shutdown(socket.SHUT_RD)
			# # print(parse.req(data.decode()));
			# # CONN.sendall(b'

			# parsed = parse.req(data.decode())
			# print(parsed['url'])

			serve_master(CONN);
			
			# try:
			# 	with open("res"+parsed["url"], mode='rb', buffering=BUFFER_SIZE) as f:
			# 		CONN.send(f.read())
					
			# except FileNotFoundError as f_err:
			# 	pass
			
			# CONN.shutdown(socket.SHUT_RDWR)
			# # time.sleep(1);
			# CONN.close()
			print(CONN)
			break
			# SERVER_SOCKET.close();

