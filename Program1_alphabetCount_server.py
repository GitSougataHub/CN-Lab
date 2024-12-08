'''write server program and a client program in python where the client sends a word to the server ,
the server counts the number of alphabets in the word and sends back to the client'''



import socket


def start_server(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server listening on {host}:{port}")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected by {addr}")
                data = conn.recv(1024).decode('utf-8')
                if not data:
                    break
                print(f"Received word: {data}")

                # Count the number of alphabets in the word
                alphabet_count = sum(c.isalpha() for c in data)

                # Send the result back to the client
                conn.sendall(str(alphabet_count).encode('utf-8'))
                print(f"Sent back count: {alphabet_count}")


if __name__ == "__main__":
    start_server()
