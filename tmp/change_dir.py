import os

while True:

    os.system("dir")
    user_input = input("select path: ")

    if user_input[:2] == 'cd':
        if os.path.exists(str(user_input[3:].replace('\n', ''))):
            os.chdir(str(user_input[3:].replace('\n', '')))
