'''write server and a client program in python to demonstrate the use of echo server'''

import socket


def start_echo_server(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Echo server running on {host}:{port}")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    # Receive data from the client
                    data = conn.recv(1024)
                    if not data:
                        break

                    message = data.decode('utf-8')
                    print(f"Received: {message}")

                    # Echo the data back to the client
                    conn.sendall(data)
                    print(f"Echoed: {message}")


if __name__ == "__main__":
    start_echo_server()
