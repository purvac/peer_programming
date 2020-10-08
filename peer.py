import select
import errno
import sys
import socket

HEADER_LENGTH = 10

if len(sys.argv) != 2:
    print('Incorrect input: Only 1 argument can be passed, you have passed ', len(server_port)-1)
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

if "connect" in input_command:
    if len(input_command) != 3:
        print(incorrect input)

host = socket.gethostname()
#IP = socket.gethostname()
server_port = 12345
client_port = 12346

def receive_message(client_socket):

    try:
        message_header = client_socket.recv(HEADER_LENGTH)

        if not len(message_header):
            return False

        message_length = int(message_header.decode('utf-8').strip())

        return {'header': message_header, 'data': client_socket.recv(message_length)}

    except:
        return False


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IPAddr, server_port))
server_socket.listen()

sockets_list = [server_socket]

while True:
    read_sockets, _, _ = select.select(timeout=0)

    #print("list of incoming connections:", read_sockets)

    for socket in read_sockets:
        if socket == server_socket:
            peer_socket, address = server_socket.accept()      #clientsocket is socket object and address is ip address
            print(f"Connection with client {address} has been established!")
            user = receive_message(peer_socket)
            if user is False:   #client disconnected before he sent his name
                    continue
            sockets_list.append(client_socket)

        else:   #existing socket is sending a message
            # Receive message
            message = receive_message(notified_socket)

            # If False, client disconnected, cleanup
            if message is False:
                print('Closed connection from: {}'.format(clients[notified_socket]['data'].decode('utf-8')))

        msg = f'{len(msg):< {HEADERSIZE}}' + msg


#**************************Peer side****************************************
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((peer_IP, peer_port))


