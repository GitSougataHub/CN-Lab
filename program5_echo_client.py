'''write server and a client program in python to demonstrate the use of echo server'''

import socket


def send_message_to_echo_server(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print(f"Connected to echo server at {host}:{port}")

        while True:
            # Input a message to send to the server
            message = input("Enter a message (type 'exit' to quit): ").strip()
            if message.lower() == "exit":
                print("Closing connection.")
                break

            client_socket.sendall(message.encode('utf-8'))
            print(f"Sent: {message}")

            # Receive the echoed message from the server
            data = client_socket.recv(1024).decode('utf-8')
            print(f"Echoed back: {data}")


if __name__ == "__main__":
    send_message_to_echo_server()
