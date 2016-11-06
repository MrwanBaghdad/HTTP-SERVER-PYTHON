
# import sys;

# def main():
#     f=open('res/index.html');
#     li=[x.encode() for x in f.readlines()];
#     print(li);




# import re;
# x="GET /banana/dasd/asd/asd.html HTTP/1.1"

# # print(re.search("(/\w*)+(.\w*)? ",x).group());
# p=[];

# import os;

# print(sys.argv);

# import socket;
# import time;
# import os;
# with open("res/index.html",mode='r',buffering=1024) as f:
#     print(f.read())

# #Serving files buffereing with http 1.0:

# def serving_http_1.0():
#     flag=False
#     try:
#         with open(parserd['url'],mode='r',buffering=conn_buffer_size) as File:
#             if not flag :
#                 conn.sendall(serv_http_1.0_header("OK"))
#                 flag=True;
#             conn.sendall(File.open().encode()) # if raw send without encoding 
#         conn.shutdown(socket.SHUT_RD);
#     except FileNotFoundError as X:
#         serv_http_1.0_header("NOT FOUND");
#     time.sleep(0.5);
#     conn.close();

# def serv_http_1.0_header(arg):
#     if arg.upper() =="OK":
#         headr_str= "HTTP /1.0 200 OK"
#         return headr_str.encode();
#     elif arg.upper() =="NOT FOUND":
#         headr_str = "HTTP /1.0 404 NOT FOUND"


def out():
    with open("res/index.html",buffering=-10) as f:
        x=f.readline();
        print(x);
        return

out()