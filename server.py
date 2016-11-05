import socket;
import re;
import os;
import parse;
import time;



#  TODO: generate a proper http response;
#  TODO: serving files and closing the connections.



host=''
port= 5007

index_html = open('res/index.html');
index_byte=[x.encode() for x in index_html.readlines()];

print(index_byte);

queue= {};


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
            for byte_line in index_byte:
                conn.send(byte_line );
            conn.close();
            time.sleep(3);
            server_socekt.close();

            break;
            # else:
            #     print(data.decode());
            #     conn.sendall(data);
            
            if not data:break;
            conn.sendall(b'200 ok');