#!/usr/bin/env python3
import socket
import os

HOST, PORT = '0.0.0.0', 9999

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
        srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        srv.bind((HOST, PORT))
        srv.listen(1)
        print(f"[Server] Listening on {HOST}:{PORT}")

        conn, addr = srv.accept()
        with conn:
            print(f"[Server] Connection from {addr}")
            req = b''
            while not req.endswith(b'\n'):
                chunk = conn.recv(1)
                if not chunk: return
                req += chunk
            _, filename = req.decode().strip().split()
            if not os.path.isfile(filename):
                conn.sendall(b"ERROR File not found\n")
                return
            data = open(filename, 'rb').read()
            header = f"OK {len(data)}\n".encode()
            conn.sendall(header)
            conn.sendall(data)
            print(f"[Server] Sent {filename} ({len(data)} bytes)")

if __name__ == '__main__':
    main()
