from socket import socket
from json import loads
from base64 import b64encode


def main():
    client = socket()
    client.connect(('192.168.1.103', 5566))
    in_data = bytes()
    data = client.recv(1024)
    while data:
        in_data += data
        data = client.recv(1024)
    my_dict = loads(in_data.decode('utf-8'))
    filename = my_dict['filename']
    filedata = my_dict['filedata'].encode('utf-8')
    with open('/home/nilv/python/' + filename, 'wb') as f:
        f.write(b64encode(filedata))
    print('over')


if __name__ == '__main__':
    main()
