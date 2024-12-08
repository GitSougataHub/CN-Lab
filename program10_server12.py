'''write a server and two client programs in python where the clients can exchange messages via server'''



import socket
import threading

# Dictionary to store connected clients
clients = {}

def handle_client(client_socket, client_address):
    """Handles communication with a connected client."""
    print(f"New connection from {client_address}")
    client_socket.send("Welcome! Type your name:".encode('utf-8'))
    client_name = client_socket.recv(1024).decode('utf-8')
    clients[client_name] = client_socket
    client_socket.send(f"Hello {client_name}! You can now send messages. Type 'exit' to disconnect.".encode('utf-8'))

    while True:
        try:
            # Receive a message from the client
            message = client_socket.recv(1024).decode('utf-8')
            if message.lower() == "exit":
                print(f"{client_name} has disconnected.")
                client_socket.send("You have been disconnected.".encode('utf-8'))
                break

            # Parse and forward message to the intended recipient
            if ":" in message:
                recipient_name, msg_content = map(str.strip, message.split(":", 1))
                if recipient_name in clients:
                    recipient_socket = clients[recipient_name]
                    recipient_socket.send(f"Message from {client_name}: {msg_content}".encode('utf-8'))
                else:
                    client_socket.send(f"Error: {recipient_name} is not connected.".encode('utf-8'))
            else:
                client_socket.send("Error: Invalid message format. Use 'recipient: message'.".encode('utf-8'))

        except ConnectionResetError:
            print(f"{client_name} has unexpectedly disconnected.")
            break

    # Cleanup after the client disconnects
    del clients[client_name]
    client_socket.close()

def start_server(host='0.0.0.0', port=65432):
    """Starts the server to handle client connections."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server running on {host}:{port}")

        while True:
            client_socket, client_address = server_socket.accept()
            threading.Thread(target=handle_client, args=(client_socket, client_address)).start()

if __name__ == "__main__":
    start_server()
