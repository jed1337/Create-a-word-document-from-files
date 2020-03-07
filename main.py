from path import Path


def print_all_files(path):
    if(path.isdir()):
        print(f"{path} is a directory")
        for sub_path in path.listdir():
            print_all_files(sub_path)
    elif(path.isfile()):
        print(f"{path} is a file")

def get_sub_directories(path):
    return [sub_path.name for sub_path in path.listdir()]

root_directory = Path(r"D:\path")
print_all_files(root_directory)

