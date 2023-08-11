import socket

def run_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Server is listening on", host, "port", port)

    conn, addr = server_socket.accept()
    print("Connected by", addr)

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("Received message:", data)
        conn.sendall(data.encode())

    conn.close()

def main():
    host = 'localhost'
    port = 1234
    run_server(host, port)

if __name__ == '__main__':
    main()