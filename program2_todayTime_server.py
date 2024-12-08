'''write a daytime server program and a daytime client program in python
where the server returns only today's time'''

import socket
from datetime import datetime


def start_daytime_server(host='127.0.0.1', port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Daytime server running on {host}:{port}")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected by {addr}")
                # Get the current time
                current_time = datetime.now().strftime("%H:%M:%S")
                print(f"Sending time: {current_time}")
                # Send the time to the client
                conn.sendall(current_time.encode('utf-8'))


if __name__ == "__main__":
    start_daytime_server()
