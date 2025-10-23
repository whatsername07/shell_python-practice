import sys
import os
import subprocess

def main():
        PATH = ""
        builtin = ["echo", "exit", "type"]
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
                    main()
            else:
                print(command_name + ": not found")

        elif (command not in builtin):
            commandList = command.split()
            custom_exe = commandList[0]
            if len(commandList) != 1:
                print("Program was passed "+ str((len(commandList))) + " args (including program name)." )
                print("Arg #0 (program name): " + commandList[0])
                x=1
                while x != len(commandList):
                    print("Arg #"+str(x)+": "+commandList[x])
                    x += 1
                subprocess.run(commandList, shell=True)
    
            #elif commandList == custom_exe:
             #   print ("Program was passed 1 args (including program name)")
              #  subprocess.run([commandList[0]])
            else:
                print(f"{custom_exe}: command not found")
                
        elif ("exit" in command):
            exit()
              
        elif ("echo" in command):
            print(command[5:])
        
        else:     
            print(f"{command}: command not found")
        main()


if __name__ == "__main__":
    main()
