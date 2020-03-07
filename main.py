from path import Path


def print_all_files(input):
    if(input.isdir()):
        for sub_directory in input.listdir():
            print(f"{sub_directory} is a sub directory")
            print_all_files(sub_directory)
    elif(input.isfile()):
        print(f"{input} is a file")


root_directory = Path(r"D:\path")
print_all_files(root_directory)

