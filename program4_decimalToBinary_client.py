'''write a server and a client program in python where the client sends a decimal number,
the server converts it into binary and sends the same to the client'''

import socket


def send_decimal_to_server(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print(f"Connected to binary conversion server at {host}:{port}")

        while True:
            # Input decimal number to send to the server
            message = input("Enter a decimal number (type 'exit' to quit): ").strip()
            if message.lower() == "exit":
                print("Closing connection.")
                break

            client_socket.sendall(message.encode('utf-8'))
            print(f"Sent: {message}")

            # Receive the binary representation from the server
            data = client_socket.recv(1024).decode('utf-8')
            print(f"Received: {data}")


if __name__ == "__main__":
    send_decimal_to_server()
