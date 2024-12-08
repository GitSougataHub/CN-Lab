'''write a server and a client program in python where the client sends a number to the server,
the server counts the number of digits and sends back the result to the client'''

import socket


def start_server(host='0.0.0.0', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server running on {host}:{port}")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connection established with {addr}")

                # Receive number from the client
                data = conn.recv(1024).decode('utf-8')
                if not data:
                    break
                print(f"Received number: {data}")

                # Count digits in the received number
                if data.isdigit():
                    digit_count = len(data)
                    response = f"Number of digits: {digit_count}"
                else:
                    response = "Error: Input is not a valid number."

                # Send the response back to the client
                conn.sendall(response.encode('utf-8'))
                print(f"Sent response: {response}")


if __name__ == "__main__":
    start_server()
