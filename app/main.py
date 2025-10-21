import sys


def main():
        sys.stdout.write("$ ")

        # Wait for user input
        command = input()
        if ("exit" in command):
            exit()
              
        if ("echo" in command):
            print(command[5:])
             
        main()


if __name__ == "__main__":
    main()
