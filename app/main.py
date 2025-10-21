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
            command_name = command[5:]
            path_env = os.environ.get("PATH", "")
            directories = path_env.split(":")
            for directory in directories:
                full_path = os.path.join(directory, command_name)
                if os.path.exists(full_path) and os.access(full_path, os.X_OK):
                     print(f"{command_name} is {full_path}")
                else:
                    print(command_name + ": not found")

        elif ("exit" in command):
            exit()
              
        elif ("echo" in command):
            print(command[5:])
        
        else:     
            print(f"{command}: command not found")
        main()


if __name__ == "__main__":
    main()
