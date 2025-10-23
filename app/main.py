import sys
import os
import subprocess

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
            # assigns a variable to the desired command name
            command_name = command[5:]
            # assigns the current directory to the variable path_env
            path_env = os.environ.get("PATH", "")
            # splits the directory into a list of individual files separated by colons
            directories = path_env.split(":")
            # loops through every file in the directory
            for directory in directories:
                # joins the user's command input to the current file in the directory
                full_path = os.path.join(directory, command_name)
                # checks the conjoined path exists and that is can be executed
                if os.path.exists(full_path) and os.access(full_path, os.X_OK):
                    # outputs file location in directory
                    print(f"{command_name} is {full_path}")
                    main()
            # if not
            else:
                # command cannot be found
                print(command_name + ": not found")

        elif (command not in builtin):
            commandList = command.split()
            custom_exe = commandList[0]
            if commandList.len() == 1:
                subprocess.run(commandList[0])
            else:
                args = []
                argsLeft = commandList.len()-1
                while argsLeft != 0:
                    i = 0
                    args.append(commandList[i])
                    argsLeft -= 1
                subprocess.run(custom_exe, args)
            

        elif ("exit" in command):
            exit()
              
        elif ("echo" in command):
            print(command[5:])
        
        else:     
            print(f"{command}: command not found")
        main()


if __name__ == "__main__":
    main()
