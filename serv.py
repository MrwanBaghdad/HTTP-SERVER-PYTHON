import socket;
import re;
import os;
import parse;
import time;


host=''
port= 5007



server_socekt= socket.socket(socket.AF_INET, socket.SOCK_STREAM);
server_socekt.bind( (host,port) );

while(1):
    server_socekt.listen(1);
    conn,addr=server_socekt.accept();
    with conn:
        print('connected by ',addr);
        while True:
            data=conn.recv(1024)
            conn.shutdown(socket.SHUT_RD);
            # print(parse.req(data.decode()));
            # conn.sendall(b'
            
            parsed=parse.req(data.decode())
            print(parsed);
            #TODO: catch FileNotFoundError;
            with open("res"+parsed["url"],mode='r',buffering=1024) as f:
                conn.sendall(f.read().encode());

            conn.shutdown(socket.SHUT_RDWR);
            # time.sleep(1);
            conn.close();
            print(conn);
            break;
            # server_socekt.close();

def serve_get(conn,url):
    with conn:
        try:
            with open(url,mode='r',buffering=1024) as f:
                x=f.read()
                conn.send(x.encode())
        except FileNotFoundError as err:
            conn.sendall(b'404 NOT FOUND')
            return

# TODO: change 1024 to buffer_size
def serve_post(conn,url):
    with conn:
        with open(url,mode='w+',buffering=1024) as f:
            data=conn.recv(1024);
            data=data.decode();
            f.write(data);

def serve_master(conn,data):
    p= parse.req(data.decode());
    if p['method'] == "GET":
        serve_get(p['url']);
    else if p['method']=="POST":
        conn.sendall(b"200 OK");
        serve_post(conn,p['url'])