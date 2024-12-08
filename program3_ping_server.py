'''write a server and a client program in python to demonstrate the use of ping program'''



import socket


def start_ping_server(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Ping server is running on {host}:{port}")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    # Receive the "ping" message from the client
                    data = conn.recv(1024).decode('utf-8')
                    if not data:
                        break
                    print(f"Received: {data}")

                    # Respond with "pong" if "ping" is received
                    if data.lower() == "ping":
                        conn.sendall("pong".encode('utf-8'))
                        print("Sent: pong")
                    else:
                        conn.sendall("Invalid message".encode('utf-8'))
                        print("Sent: Invalid message")


if __name__ == "__main__":
    start_ping_server()
