import sys


def main():
    x=1
    while x==1:
        sys.stdout.write("$ ")

        # Wait for user input
        command = input()
        print(f"{command}: command not found")


if __name__ == "__main__":
    main()
