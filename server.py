import socket

def get_weight(member_name):
    return {
        'nayeon' : '48',
        'jeongyeon' : '49',
        'momo' : '46',
        'sana' : '48',
        'jihyo' : '45',
        'mina' : '45',
        'dahyun' : '48',
        'chaeyoung' : '46',
        'tzuyu' : '51',
    }.get(member_name)

def get_height(member_name):
    return {
        'nayeon' : '163',
        'jeongyeon' : '167',
        'momo' : '162',
        'sana' : '163',
        'jihyo' : '160',
        'mina' : '164',
        'dahyun' : '158',
        'chaeyoung' : '159',
        'tzuyu' : '171',
    }.get(member_name)

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_sock.bind(('0.0.0.0', 12345))
server_sock.listen(0)

client_sock, addr = server_sock = server_sock.accept()
data = client_sock.recv(65535)

uri = data.decode()
protocol = uri.split(':')[0]
member_name = uri.split('/')[2]
request_data = uri.split('/')[3]

if protocol == "twice":
    if request_data == "height":
        try:
            client_sock.send(("height:" + member_name + ":" + get_height(member_name)).encode())
        except AttributeError:
            client_sock.send("error:404:member".encode())
    elif request_data == "weight":
        try:
            client_sock.send(("weight:" + member_name + ":" + get_weight(member_name)).encode())
        except AttributeError:
            client_sock.send("error:404:member".encode())
    else:
        client_sock.send("error:404:request".encode())
else:
    client_sock.send("error:404:protocol".encode())