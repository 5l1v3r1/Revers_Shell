# Revers_Shell

### What Do

- Working on v1.4
- use v1.2 for test

### Working On
- Change directory [cd]
- Upload File [upload]
- Download File 

### News Features
- [cd /] (Go directly to C /)
- [exit] (Close Connection)

### Correction
- v1.4 more stable than v1.2
- More error handle (Empty Command, Command not Handle)
- Duplicate command line output handle


### Issue
- Cant change directory easly

### To Know

In target.py this part of code is using for debug and targeting command process and error
``
    # Test block
    print("rcv_command:", rcv_command)
    print("op_pid:", op.pid)
    print("op_wait:", op.wait())  # if op.wait is at 1 thats mean the command is not handle or understand
    print("------------------------")
    # End Of Test Block
``
