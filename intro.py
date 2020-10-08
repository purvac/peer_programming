import sys
import socket

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

if input_command == "myip":
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    #print("Your Computer Name is:" + hostname)
    print("Your Computer IP Address is:" + IPAddr)

if input_command == "myport":
    print(server_port)

if "connect" in input_command:
    if len(input_command) != 3:
        print(incorrect input)
