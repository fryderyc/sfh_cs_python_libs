import socket

def run_client(host, port, message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    client_socket.sendall(message.encode())
    print("Sent message:", message)

    response = client_socket.recv(1024).decode()
    print("Received response:", response)

    client_socket.close()

def main():
    host = 'localhost'
    port = 1234
    message = input("Enter your message: ")
    run_client(host, port, message)

if __name__ == '__main__':
    main()