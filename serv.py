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
            # print(parse.req(data.decode()));
            # conn.sendall(b'
            for i in range(1,3):
                conn.send(b'heelwo');
                time.sleep(2);
            
            conn.shutdown(socket.SHUT_WR);
            conn.shutdown(socket.SHUT_RDWR);
            # time.sleep(1);
            conn.close();
            print(conn);
            break;
            # server_socekt.close();
            