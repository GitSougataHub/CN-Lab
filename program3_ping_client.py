'''write a server and a client program in python to demonstrate the use of ping program'''



import socket


def ping_server(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print(f"Connected to ping server at {host}:{port}")

        while True:
            # Send a "ping" message to the server
            message = input("Enter message (type 'exit' to quit): ").strip()
            if message.lower() == "exit":
                print("Closing connection.")
                break

            client_socket.sendall(message.encode('utf-8'))
            print(f"Sent: {message}")

            # Receive the server's response
            data = client_socket.recv(1024).decode('utf-8')
            print(f"Received: {data}")


if __name__ == "__main__":
    ping_server()
