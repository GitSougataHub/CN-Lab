'''write a server and a client program in python to demonstrate byte ordering'''


import socket
import struct


def start_byte_order_server(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Byte order server running on {host}:{port}")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected by {addr}")
                try:
                    # Receive 4 bytes (integer in network byte order)
                    data = conn.recv(4)
                    if not data:
                        print(f"Connection closed by {addr}")
                        break

                    # Unpack the received data as a 4-byte integer (big-endian)
                    received_value = struct.unpack('!I', data)[0]
                    print(f"Received value (big-endian): {received_value}")

                    # Convert to little-endian
                    little_endian_value = struct.unpack('<I', data)[0]
                    print(f"Interpreted value (little-endian): {little_endian_value}")

                    # Send results back to the client
                    response = f"Big-endian: {received_value}, Little-endian: {little_endian_value}"
                    conn.sendall(response.encode('utf-8'))
                except Exception as e:
                    print(f"Error: {e}")
                    break


if __name__ == "__main__":
    start_byte_order_server()
