'''write a server and two client programs in python where the clients can exchange messages via server'''




import socket
import threading

def receive_messages(client_socket):
    """Handles incoming messages from the server."""
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(message)
        except ConnectionResetError:
            print("Disconnected from server.")
            break

def start_client(host='127.0.0.1', port=65432):
    """Starts the client to connect to the server."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            client_socket.connect((host, port))
            print("Connected to the server.")

            # Start a thread to receive messages
            threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

            # Send messages to the server
            while True:
                message = input()
                client_socket.sendall(message.encode('utf-8'))
                if message.lower() == "exit":
                    break
        except ConnectionRefusedError:
            print("Unable to connect to the server.")

if __name__ == "__main__":
    start_client()
