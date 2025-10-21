import sys


def main():
        sys.stdout.write("$ ")

        # Wait for user input
        command = input()
        if ("exit" in command):
            exit()
              
        print(f"{command}: command not found")
        main()


if __name__ == "__main__":
    main()
