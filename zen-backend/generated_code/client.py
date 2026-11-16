import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()
port = 12345

# Connect to the server
client_socket.connect((host, port))

# Send request
request = 'Hello, world!'
client_socket.sendall(request.encode())

# Get response
response = client_socket.recv(1024)
print('Server response:', response.decode())
client_socket.close()