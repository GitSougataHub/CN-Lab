'''write a server and a client program in python where the client sends a decimal number,
the server converts it into binary and sends the same to the client'''

import socket


def start_binary_server(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Binary conversion server running on {host}:{port}")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    # Receive the decimal number from the client
                    data = conn.recv(1024).decode('utf-8')
                    if not data:
                        break

                    print(f"Received decimal number: {data}")

                    # Convert the decimal number to binary
                    try:
                        decimal_number = int(data)
                        binary_representation = bin(decimal_number)[2:]  # Remove '0b' prefix
                        conn.sendall(binary_representation.encode('utf-8'))
                        print(f"Sent binary: {binary_representation}")
                    except ValueError:
                        conn.sendall("Invalid number".encode('utf-8'))
                        print("Sent: Invalid number")


if __name__ == "__main__":
    start_binary_server()
