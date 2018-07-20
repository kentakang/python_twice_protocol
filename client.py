import socket

def member_name_to_korean(member_name):
    return {
        'nayeon' : '나연',
        'jeongyeon' : '정연',
        'momo' : '모모',
        'sana' : '사나',
        'jihyo' : '지효',
        'mina' : '미나',
        'dahyun' : '다현',
        'chaeyoung' : '채영',
        'tzuyu' : '쯔위',
    }.get(member_name)

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_sock.connect(('localhost', 12345))
print("요청 할 URL을 입력해주세요.")
print("ex) twice://member_name/request")
print("멤버 목록 : nayeon, jeongyeon, chaeyoung, tzuyu, jihyo, dahyun, momo, sana, mina")
print("요청 가능 목록 : 키 (height), 몸무게 (weight)")
url = input("URL : ")

client_sock.send(url.encode())
data = client_sock.recv(65535)
response_format = data.decode().split(":")[0]
response_member = data.decode().split(":")[1]
response_data = data.decode().split(":")[2]

if (response_format == "height"):
    if (int(response_data) >= 160):
        msg = "키가 크네요"
    else:
        msg = "키가 작네요"
    
    print(member_name_to_korean(response_member) + "의 키는 " + response_data + "cm입니다. " + msg)
elif (response_format == "weight"):
    if (int(response_data) >= 50):
        msg = "몸무게가 많이 나가네요"
    else:
        msg = "몸무게가 적게 나가네요"

    print(member_name_to_korean(response_member) + "의 몸무게는 " + response_data + "kg입니다. " + msg)
else:
    if (response_data == "protocol"):
        print("지원하지 않는 프로토콜입니다.")
    elif (response_data == "request"):
        print("요청 불가능 한 항목입니다.")
    elif (response_data == "member"):
        print("멤버 이름을 잘못 입력하셨습니다.")
    else:
        print("알 수 없는 오류입니다.")