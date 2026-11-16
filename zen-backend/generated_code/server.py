import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()
port = 12345

# Bind to the port
server_socket.bind((host, port))

# Queue up to 5 requests
server_socket.listen(5)

while True:
    # Wait for client connection
    client_connection, client_address = server_socket.accept()
    print('Got a connection from:', client_address)
    # Now do some crypto magic
    request = client_connection.recv(1024)
    print('Client requested:', request)
    # Send back a response
    client_connection.sendall('Hello, world!'.encode())
    client_connection.close()