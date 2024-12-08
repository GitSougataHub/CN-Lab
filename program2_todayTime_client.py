'''write a daytime server program and a daytime client program in python
where the server returns only today's time'''



import socket


def get_daytime_from_server(host='127.0.0.1', port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print(f"Connected to daytime server at {host}:{port}")

        # Receive the current time from the server
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Received time: {data}")


if __name__ == "__main__":
    get_daytime_from_server()
