import re
import socket
import sys
import time
from os import mkdir
import parse;
# method = sys.argv[1] ;
# file_name= sys.argv[2];
method="GET"
file_name= "index.html"

#setting defulats host and port num

try:
    host=sys.argv[3];
except IndexError as err:
    host='localhost';

try:
    port=sys.argv[4];
except IndexError as s:
    port=5007;

#initiate connection


s=  socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
s.connect((host,port))

x=1;

#creating string using literals
req_s="%s /%s HTTP/1.0 "
data = req_s %(method.upper(),file_name) 

s.sendall(data.encode());


rcvdata='';

if method.upper() == "GET":
    s.sendall(data.encode())
    while True:
    data=s.recv(1024).decode();
    print(data);
    if data == '':
        s.shutdown(socket.SHUT_RDWR)
        s.close();
        break;
    else:
        rcvdata+=data;
    # time.sleep(2);

# TODO: get how to pass buffer as argument or don't use one :D
def write_to_desk(file_name,buffer):
    with s:
        with open("clientres/"+file_name,mode='w+',buffer=1024) as file:
            data=s.recv().decode();
            file.write(data);
            if data=='':
                s.shutdown(socket.SHUT_RDWR);
                return;

def traverse(file_name):
    #TODO parse file's contents send gets till complete
    # TODO: recursiion or not recursion
    url=[];
    if file_name.endswith('.txt'):
        # with open("clientres/"+file_name,'w+') as file:
            x=file.readlines();
            for l in x:
                parsed=parse.req(l);
                url.append(( parsed['method'], parsed['url'] ))


def get_req(url):
    s.sendall(req_s % ("GET",url));

def post_req(url,file_name):
    s.sendall(req_s % ("POST",url));
    data=s.recv(1024)
    if !data.upper()=='200 OK':
        return ConnectionError;
    with s:
        with open("clientres/"+url,mode='r',buffering=1024) as f:
            x=f.read()
            s.sendall(x.encode())
