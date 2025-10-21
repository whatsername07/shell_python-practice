import sys


def main():
        builtin = ["echo", "exit"]
        sys.stdout.write("$ ")

        # Wait for user input
        command = input()
        if ("exit" in command):
            exit()
              
        elif ("echo" in command):
            print(command[5:])

        elif (command in builtin):
             print(f"{command} is a shell builtin")
        else:     
            print(f"{command}: command not found")
        main()


if __name__ == "__main__":
    main()
