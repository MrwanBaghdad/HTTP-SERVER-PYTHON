import socket;
import time;
import sys;
from os import mkdir




method = sys.argv[1];
file_name= sys.argv[2];

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
data = "%s /%s/ HTTP /1.0 " %(method,file_name) 

s.sendall(data.encode());


rcvdata='';
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
if rcvdata != '':
    f=open("clientres"+file_name, mode='w+')
    f.write(rcvdata);
else
    print("NOTHING")

