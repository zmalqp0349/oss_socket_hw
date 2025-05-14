import socket

HOST = '127.0.0.1'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((HOST, PORT))

server_socket.listen()

print(f"Echo 서버 시작: {HOST}:{PORT}에서 클라이언트 연결 대기중...")

client_socket, client_addr = server_socket.accept()
print(f"{client_addr}와 연결되었습니다.")

while True:
    data = client_socket.recv(1024)
    if not data:
        break
    received_str = data.decode('utf-8')
    print(f"클라이언트로부터 받은 메시지: {received_str}")
    client_socket.sendall(data)

print("클라이언트 연결 종료. 서버를 종료합니다.")
client_socket.close()
server_socket.close()
