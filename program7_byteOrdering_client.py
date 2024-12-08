'''write a server and a client program in python to demonstrate byte ordering'''


import socket
import struct


def communicate_with_server(host='127.0.0.1', port=65432):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))
            print(f"Connected to byte order server at {host}:{port}")

            while True:
                try:
                    # Get an integer from the user
                    user_input = input("Enter an integer (type 'exit' to quit): ").strip()
                    if user_input.lower() == "exit":
                        print("Closing connection.")
                        break

                    # Validate and pack the integer in big-endian format
                    number = int(user_input)
                    packed_data = struct.pack('!I', number)

                    # Send the packed data to the server
                    client_socket.sendall(packed_data)
                    print(f"Sent: {number} (big-endian)")

                    # Receive the response from the server
                    response = client_socket.recv(1024).decode('utf-8')
                    print(f"Server Response: {response}")
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")
                except Exception as e:
                    print(f"Error: {e}")
                    break
    except socket.error as e:
        print(f"Socket error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    communicate_with_server()
