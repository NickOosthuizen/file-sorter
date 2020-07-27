import os

class Root_Directory():
    def __init__(self, read_file):
        self.path = ""
        self.file_associations = {}
        self.get_file_associations(read_file) 

    def get_file_associations(self, read_file):
        f = open(read_file, "r")

        if f.mode == "r":
            lines = f.readlines()
            lines = [line.rstrip('\n') for line in lines]
            self.path = lines[0]
            if not os.path.isdir(self.path):
                raise OSError("Specified path to sort is not a directory")
            self.file_associations["other"] = "other_files"
            self.file_associations["dir"] = "directories"
            try:
                lines[1]
            except IndexError:
                f.close()
                return
            for line in lines[1:]:
                type_dict_pair = line.split(" - ")
                if type_dict_pair[0][0] != ".":
                    continue
                if len(type_dict_pair) == 2:
                    self.file_associations[type_dict_pair[0]] = type_dict_pair[1]
        f.close()

    def update_child_directories(self):
        current_files = os.listdir(self.path)
        for dict_name in self.file_associations.values():
            if dict_name not in current_files:
                dir_path = os.path.join(self.path, dict_name)
                current_files.append(dict_name)
                os.mkdir(dir_path)
    
    def sort_files(self):
        current_files = os.listdir(self.path)
        for file_name in current_files:
            if file_name not in self.file_associations.values():
                (file_ext, new_file_name) = self.resolve_file_name(file_name)
                old_path = os.path.join(self.path, file_name)
                new_path = os.path.join(self.path, self.file_associations[file_ext], new_file_name)
                os.rename(old_path, new_path)
    
    def resolve_file_name(self, file_name):
        split_name = file_name.split(".")
        file_ext = "." + split_name[-1]
        if file_ext not in self.file_associations:
            file_ext = "other"
        if os.path.isdir(os.path.join(self.path, file_name)):
            file_ext = "dir"
        files_in_dir = os.listdir(os.path.join(self.path, self.file_associations[file_ext]))
        i = 1
        split_name.insert(1, "")
        while file_name in files_in_dir:
            split_name[1] = ("(" + str(i) + ")")
            file_name = "".join(split_name[0:2])
            if len(split_name) > 2:
                file_name += "." + ".".join(split_name[2:])
            i += 1
        return file_ext, file_name

def main():
    root = Root_Directory("template.txt")
    root.update_child_directories()
    root.sort_files()

if __name__ == "__main__":
    main()


    
            
