import sys


def main():
        sys.stdout.write("$ ")

        # Wait for user input
        command = input()
        if ("exit" in command):
            exit()
              
        elif ("echo" in command):
            print(command[5:])

        else:     
            print(f"{command}: command not found")
        main()


if __name__ == "__main__":
    main()
