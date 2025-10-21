import sys
import os

def main():
        PATH = ""
        builtin = ["echo", "exit", "type"]
        sys.stdout.write("$ ")

        # Wait for user input
        command = input()
        # if the input contains 'type' and the word after type is a builtin command
        if ("type" in command and command[5:] in builtin):
            # output that it is a builtin command
            print(command[5:] + " is a shell builtin")
        
        # if the input contains 'type' and the second part is not a builtin command
        elif ("type" in command and command[5:] not in builtin):
            if os.path.exists(PATH):
                # list the files in the directory
                fileList = os.listdir(PATH)
                # if the file is in the directory
                for i in fileList:
                    if i == command[5:]:
                        print(i + " is " + PATH)
                        break
            else:
                # print that the file is not found
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
