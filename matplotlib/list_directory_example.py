import os

def list_directory_example():
    files = os.listdir('.')
    print(files)

if __name__ == "__main__":
    list_directory_example()
