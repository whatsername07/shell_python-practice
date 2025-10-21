import sys
import os

def main():
        #PATH = "./bin:./sbin"
        PATH = os.environ['PATH']
        builtin = ["echo", "exit", "type"]
        sys.stdout.write("$ ")

        # Wait for user input
        command = input()
        if ("type" in command and command[5:] in builtin):
            print(command[5:] + " is a shell builtin")
        
        elif ("type" in command and command[5:] not in builtin):
            for path in PATH.split(":"):
                absPath = os.path.abspath(path)
                pathToExe = None
                if not os.path.exists(absPath):
                     break#path doesn't exist
                for file in os.listdir(absPath):#loops through files in current environment path
                     if file == command[5:].split(" ")[0]:#checks if file equal executable name
                          pathToExe = absPath + "/" + file
                          break
                if pathToExe != None:
                     break
            print(command[5:] + " is " + pathToExe )

        elif ("exit" in command):
            exit()
              
        elif ("echo" in command):
            print(command[5:])
        
        else:     
            print(f"{command}: command not found")
        main()


if __name__ == "__main__":
    main()
