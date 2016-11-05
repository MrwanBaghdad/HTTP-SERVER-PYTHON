


# f=open('req.txt',mode='r');

# r= f.readlines();
x="GET /index/banan.html HTTP/1.1 \n Host: localhost:50008 \n User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.53.11 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10  \n Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8  \n Accept-Language: en-us \n Accept-Encoding: gzip, deflate \n Connection: keep-alive"

import re;

def req(arg1):

    li=arg1.split('\n');
    # url = re.search('(\\\w)*')
    
    
    get={};
    for i in li:
        try:
            x=i.split(':',1);
            get[x[0].strip()]=x[1].strip();
        except IndexError as s:
            if(re.match('GET',i)):
                get['method']='GET';
                get['url']=re.search('(/\w*)+(.\w*)?',i).group()
                # print('-----',url) if url!=None else print('----------');
            elif (re.match('POST',i)):
                get['method']='POST';
                get['url']=re.search('(/\w*)+(.\w*)?',i).group()
            continue
    # print({'headers':get, 'url':url});
    return(get);


print(req(x))