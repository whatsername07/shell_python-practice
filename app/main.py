import sys


def main():
        sys.stdout.write("$ ")

        # Wait for user input
        command = input()
        if ("end" in command) and ("0" in command):
            return("success")
        
        if ("end" in command) and ("1" in command):
             return("error")
              
        print(f"{command}: command not found")
        main()


if __name__ == "__main__":
    main()
