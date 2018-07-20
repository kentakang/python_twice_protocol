# python_twice_protocol
## Description
TWICE Protocol (Twice member Weight and heIght Content providE Protocol)은 방학 수업 중 실습을 위해 제작 된 프로토콜입니다.
트와이스 멤버들의 키, 몸무게 정보를 제공합니다.
## Protocol Specification
ex) twice://dahyun/height
URL 형식은 twice://member_name/request_data 의 형식입니다.
### Request
Request Type | Return
----------------------
Member | nayeon, dahyun, momo, sana, tzuyu, jeongyeon, mina, chaeyoung, jihyo
Weight | 요청 한 멤버의 몸무게
Height | 요청 한 멤버의 키
### Response
ex) height:dahyun:158
응답 형식은 response_type:member_name:response_data 의 형식입니다.
Response Type | Description
---------------------------
Height | 멤버의 키를 제공합니다.
Weight | 멤버의 몸무게를 제공합니다.
Error  | 오류입니다. 
오류가 발생할 경우 error:error_code:error_name 의 형식으로 응답합니다.
Error Code | Error Name | Description
-------------------------------------
404 | protocol | 프로토콜이 twice 프로토콜이 아닐 시 발생하는 오류입니다.
404 | member | 멤버 이름이 잘못되었거나, 존재하지 않는 멤버일시 발생하는 오류입니다.
404 | request | 잘못 된 요청일 때 발생하는 오류입니다.