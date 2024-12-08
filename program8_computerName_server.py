'''write a server and a client program in python where the client ask for the name of the server,
the server replies back by sending the computer name'''

import socket


def start_server(host='0.0.0.0', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server running on {host}:{port}")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connection established with {addr}")
                # Receive a message from the client
                request = conn.recv(1024).decode('utf-8')
                if request.lower() == "get name":
                    # Send the server's computer name
                    server_name = socket.gethostname()
                    conn.sendall(server_name.encode('utf-8'))
                    print(f"Sent server name: {server_name}")
                else:
                    # Handle unknown requests
                    conn.sendall(b"Unknown request")
                    print("Unknown request received")


if __name__ == "__main__":
    start_server()
