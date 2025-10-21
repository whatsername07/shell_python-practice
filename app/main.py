import sys
import os

def main():
        PATH = ""
        builtin = ["echo", "exit", "type"]
        sys.stdout.write("$ ")

        # Wait for user input
        command = input()
        if ("type" in command and command[5:] in builtin):
            print(command[5:] + " is a shell builtin")
        
        elif ("type" in command and command[5:] not in builtin):
            if os.path.exists:
                fileList = os.listdir(PATH)
                if command[5:] in fileList:
                    print(command[5:] + " is " + PATH)
            else:
                print(command[5:] + ": not found")

        elif ("exit" in command):
            exit()
              
        elif ("echo" in command):
            print(command[5:])
        
        else:     
            print(f"{command}: command not found")
        main()


if __name__ == "__main__":
    main()
