import sys
import os
import subprocess

def main():
    PATH = ""
    builtin = ["echo", "exit", "type"]
    while True:
        
        sys.stdout.write("$ ")

        command = input()
        if ("type" in command and command[5:] in builtin):
            print(command[5:] + " is a shell builtin")
        
   
        elif ("type" in command and command[5:] not in builtin):
            command_name = command[5:]
            path_env = os.environ.get("PATH", "")
            directories = path_env.split(":")
            for directory in directories:
                full_path = os.path.join(directory, command_name)
                if os.path.exists(full_path) and os.access(full_path, os.X_OK):
                    print(f"{command_name} is {full_path}")
                    continue
                else:
                    print(command_name + ": not found")
                    continue

        elif (command not in builtin):
            commandList = command.split()
            custom_exe = commandList[0]
            if len(commandList) == 0:
                print(f"{custom_exe}: command not found")
                continue
            subprocess.run(commandList)
                
        elif ("exit" in command):
            exit()
              
        elif ("echo" in command):
            print(command[5:])
        
        else:     
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
