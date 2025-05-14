import socket

HOST = '127.0.0.1'
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
print(f"서버 {HOST}:{PORT}에 연결되었습니다.")

try:
    while True:
        msg = input("서버로 보낼 메시지 입력 (종료는 quit): ")
        if not msg:
            continue
        if msg.lower() == 'quit':
            print("quit 명령을 받아 클라이언트를 종료합니다.")
            break
        client_socket.sendall(msg.encode('utf-8'))
        data = client_socket.recv(1024)
        if not data:
            print("서버와 연결이 종료되었습니다.")
            break
        received_str = data.decode('utf-8')
        print(f"서버로부터 응답: {received_str}")
finally:
    client_socket.close()
