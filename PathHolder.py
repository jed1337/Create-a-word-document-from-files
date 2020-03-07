class PathHolder:
    def __init__(self, path):
        self.path = path
        self.script_names = []
        self.verification_script_names = []

        for sub_path in self.path.listdir():
            sub_path_files = self.get_all_files(sub_path)

            # Case insensitive string comparison
            if "verification".casefold() in str(sub_path.basename()).casefold():
                self.verification_script_names.extend(sub_path_files)
            else:
                self.script_names.extend(sub_path_files)

    def get_all_files(self, path):
        files=[]
        if(path.isdir()):
            for sub_path in path.listdir():
                files.extend(self.get_all_files(sub_path))
        elif(path.isfile()):
            files.append(path)

        return files

