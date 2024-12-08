'''write server program and a client program in python where the client sends a word to the server ,
the server counts the number of alphabets in the word and sends back to the client'''


import socket


def send_word_to_server(word, host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print(f"Connected to server at {host}:{port}")

        # Send the word to the server
        client_socket.sendall(word.encode('utf-8'))
        print(f"Sent word: {word}")

        # Receive the count from the server
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Received count: {data}")


if __name__ == "__main__":
    word = input("Enter a word to send to the server: ")
    send_word_to_server(word)
