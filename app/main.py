import sys


def main():
        builtin = ["echo", "exit", "type"]
        sys.stdout.write("$ ")

        # Wait for user input
        command = input()
        if ("type" in command and command[5:] in builtin):
            print(command[5:] + " is a shell builtin")
        
        if ("type" in command and command[5:] not in builtin):
            print(command[5:] + ": command not found")

        elif ("exit" in command):
            exit()
              
        elif ("echo" in command):
            print(command[5:])
        
        else:     
            print(f"{command}: command not found")
        main()


if __name__ == "__main__":
    main()
