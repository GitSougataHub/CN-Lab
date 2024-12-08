'''write a server and a client program in python where the client sends a number to the server,
the server counts the number of digits and sends back the result to the client'''

import socket


def send_number_to_server(host='127.0.0.1', port=65432):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))
            print(f"Connected to server at {host}:{port}")

            # Get the number from the user
            number = input("Enter a number: ")
            client_socket.sendall(number.encode('utf-8'))

            # Receive the response from the server
            response = client_socket.recv(1024).decode('utf-8')
            print(f"Response from server: {response}")
    except socket.error as e:
        print(f"Socket error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    send_number_to_server()
