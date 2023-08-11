import os

def list_files(directory):
    print("Files in", directory, ":")
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            print(filename)

def main():
    directory = input("Enter the directory path: ")
    list_files(directory)

if __name__ == '__main__':
    main()