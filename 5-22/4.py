# from socket import socket, SOCK_STREAM, AF_INET
# from datetime import datetime
#
#
# def main():
#     server = socket(family=AF_INET, type=SOCK_STREAM)
#     server.bind(('192.168.1.103', 6789))
#     server.listen(512)
#     print('服务器启动开始监听')
#     while True:
#         client, addr = server.accept()
#         print(str(addr) + '连接到了服务器')
#         client.send(str(datetime.now()).encode('utf-8'))
#         client.close()
#
#
# if __name__ == '__main__':
#     main()


from socket import socket, SOCK_STREAM, AF_INET
from base64 import b64encode
from json import dumps
from threading import Thread


def main():

    class FileTransferHandler(Thread):

        def __init__(self, cclient):
            super().__init__()
            self.cclient = cclient

        def run(self):
            my_dict = {}
            my_dict['filename'] = 'logo.png'
            my_dict['filedata'] = data
            json_str = dumps(my_dict)
            self.cclient.send(json_str.encode('utf-8'))
            self.cclient.close()


    server = socket()
    server.bind(('192.168.1.103', 5566))
    server.listen(512)
    print('服务器启动开始监听。。。')
    with open('logo.png', 'rb') as f:
        data = b64encode(f.read()).decode('utf-8')
    while True:
        client, addr = server.accept()
        FileTransferHandler(client).start()


if __name__ == '__main__':
    main()