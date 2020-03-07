from path import Path
from PathHolder import PathHolder


def print_all_files(path):
    if(path.isdir()):
        print(f"{path} is a directory")
        for sub_path in path.listdir():
            print_all_files(sub_path)
    elif(path.isfile()):
        print(f"{path} is a file")


path = Path(r"D:\path")
print_all_files(path)

path_holders = [PathHolder(sub_path) for sub_path in path.listdir()]

print(path_holders)
