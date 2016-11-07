import socket
import re
import os
import parse
import time

HOST = ''
PORT = 5007



SERVER_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER_SOCKET.bind((HOST, PORT))

while 1:
    SERVER_SOCKET.listen(1)
    CONN, ADDR = SERVER_SOCKET.accept()
    with CONN:
        print('connected by ', ADDR)
        while True:
            data = CONN.recv(1024)
            CONN.shutdown(socket.SHUT_RD)
            # print(parse.req(data.decode()));
            # CONN.sendall(b'

            parsed = parse.req(data.decode())
            print(parsed)

    # TODO : catch FileNotFoundError
            with open("res"+parsed["url"], mode='r', buffering=1024) as f:
                CONN.sendall(f.read().encode())

            CONN.shutdown(socket.SHUT_RDWR)
            # time.sleep(1);
            CONN.close()
            print(CONN)
            break
            # SERVER_SOCKET.close();

def serve_get(conn, url):
    with conn:
        try:
            with open(url, mode='r', buffering=1024) as f:
                x = f.read()
                conn.send(x.encode())
        except FileNotFoundError as err:
            conn.sendall(b'404 NOT FOUND')
            print(err)
            return

# FIXME: change 1024 to buffer_size 
def serve_post(conn, url):
    with conn:
        with open(url, mode='w+', buffering=1024) as f:
            data = conn.recv(1024)
            data = data.decode()
            f.write(data)

def serve_master(conn, data):
    p = parse.req(data.decode());
    if p['method'] == "GET":
        serve_get(conn, p['url']);
    elif p['method'] == "POST":
        conn.sendall(b"200 OK");
        serve_post(conn, p['url'])
