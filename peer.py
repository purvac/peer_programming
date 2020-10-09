import select
import errno
import sys
import socket
import selectors

HEADER_LENGTH = 10

if len(sys.argv) != 2:
    print('Incorrect input: Only 1 argument can be passed, you have passed ', len(sys.argv)-1)
    exit()

if sys.argv[1].isdigit() == False:
    print("Command line input should be a numeric value indicating the port number")
    exit()

print("Server port # = ", sys.argv[1])
print("To show the command manual, enter help.")
print("If you are already aware of the commands, enter the relevant command.")
print("Commands are case sensitive. Do not use Caps while entering the input commands")
server_port = sys.argv[1]      #command line argument that passes server port number

input_command = input()

if input_command == "help":
    print("myip: Show the ip address of your laptop")
    print("myport: Show the port number that the process runs on")
    print("connect <destination_ip> <destination_port>: Connect you to another peer to send messages to peers.")
    print("list: List all the connected peers")
    print("send <connection_id> <message>: Send given message on the given connection id mentioned in the list")
    print("terminate <connection_id>: Terminate connection with the specified connection id mentioned in the list")
    print("exit: Terminate all the connections and exit the program")
    print("\n")
    input_command = input()             #implement recursion

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
#print("Your Computer Name is:" + hostname)


if input_command == "myip":
    print("Your Computer IP Address is:" + IPAddr)

if input_command == "myport":
    print(server_port)

#sel = selectors.DefaultSelector()
#server program

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IPAddr, int(server_port)))
print("server socket: ")
print(server_socket)
server_socket.listen()
print('listening on', (IPAddr, server_port))
#lsock.setblocking(False)    #calls made to this client will no longer block
#sel.register(server_socket, selectors.EVENT_READ, data=None)    #register the socket to be monitored by sel select
#"""
def receive_message(client_socket):
    try:
        # Receive our "header" containing message length, it's size is defined and constant
        message_header = client_socket.recv(HEADER_LENGTH)
        #if not len(message_header): # If we received no data, client gracefully closed a connection
            #return "No data recvd, connection closed from client end gracefully"
        message_length = int(message_header.decode('utf-8'))    # Convert header to int value
        # Return an object of message header and message data
        #return {'header': message_header, 'data': client_socket.recv(message_length)}
        #print("Received message from " + client_address[0] + ": " + client_socket.recv(message_length))
        return message_length
    except:
        return False
#"""
sockets_list = [server_socket]

clients = []

while True:
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

    for socket in read_sockets:
        if socket == server_socket:
            client_socket, client_address = server_socket.accept()
            clients.append(client_address)
            #user = receive_message(client_socket)
            #print(clients)
            #print("Client Socket Details: ")
            #print(client_socket)
            #print(client_address)
            sockets_list.append(client_socket)
            """
            for i in range (len(sockets_list)):
                print(i, sockets_list)
                print("\n")
            """
    else:
            # Receive message
            message_length = receive_message(socket)
            # If False, client disconnected, cleanup
            if message_length != 0:
                print("Received message from " + client_address[0] + ": " + client_socket.recv(message_length).decode('utf-8'))
            else:
                print("No data recvd, connection closed from client end gracefully")
            #print(message)
            """
            if message is False:
                print('Closed connection from: ', client_address)
                # Remove from list for socket.socket()
                sockets_list.remove(socket)
                # Remove from our list of users
                print(clients)
                print(client_address)
                clients.remove(client_address)

                continue
            """
            #exit()

