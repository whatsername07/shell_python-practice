import sys
import os
import subprocess

def main():
    PATH = ""
    builtin = ["echo", "exit", "type", "pwd", "cd"]
    currentPath = os.getcwd()
    while True:
        
        sys.stdout.write("$ ")

        command = input()
        if ("type" in command and command[5:] in builtin):
            print(command[5:] + " is a shell builtin")
        
        elif ("exit" in command):
            exit()

        elif ("echo" in command):
            print(command[5:])

        elif (command == "pwd"):
            print(currentPath)

        elif (command == "cd"):
            currentPath = currentPath + command[3:]
   
        elif ("type" in command and command[5:] not in builtin):
            command_name = command[5:]
            path_env = os.environ.get("PATH", "")
            directories = path_env.split(":")
            for directory in directories:
                full_path = os.path.join(directory, command_name)
                if os.path.exists(full_path) and os.access(full_path, os.X_OK):
                    print(f"{command_name} is {full_path}")
                    break
            else: 
                print(command_name + ": not found")
                continue

        elif (command not in builtin):
            commandList = command.split()
            custom_exe = commandList[0]
            try:
                subprocess.run(commandList)
            except:
                print(f"{command}: command not found")
            continue
        
        else:     
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
