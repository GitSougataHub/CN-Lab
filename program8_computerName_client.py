import socket


def request_server_name(host='127.0.0.1', port=65432):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))
            print(f"Connected to server at {host}:{port}")

            # Send the "get name" request to the server
            client_socket.sendall(b"GET NAME")

            # Receive the server's response
            server_name = client_socket.recv(1024).decode('utf-8')
            print(f"Server name received: {server_name}")
    except socket.error as e:
        print(f"Socket error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    request_server_name()
