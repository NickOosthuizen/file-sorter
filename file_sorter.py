import os

class Root_Directory():
    def __init__(self, read_file):
        self.base_path = ""
        self.file_associations = {}
        self.get_file_associations(read_file) 

    """
    read the file passed to class to get path of file to be sorted,
    the names of directories to sort files into, and the file 
    extensions to put in those directories
    """
    def get_file_associations(self, read_file):
        f = open(read_file, "r")

        if f.mode == "r":
            lines = f.readlines()
            lines = [line.rstrip('\n') for line in lines]
            self.base_path = lines[0]
            # the first line of the file must be a directory
            if not os.path.isdir(self.base_path):
                raise OSError("Specified path to sort is not a directory")
            """
            "other" and "dir" are created by the program for directories
            and files types that are not specified in the text file. The names
            of these types' corresponding directories will be overwritten if specified
            in the text file
            """
            self.file_associations["other"] = "other_files"
            self.file_associations["dir"] = "directories"
            # there are no provided associations if there are less than 2 lines
            if len(lines) < 2:
                f.close()
                return
            for line in lines[1:]:
                # text file should have directory and file type separated by " - "
                type_dict_pair = line.split(" - ")
                if type_dict_pair[0][0] != "." and type_dict_pair[0] != "other" and type_dict_pair[0] != "dir":
                    continue
                # each line needs to only have 2 parts separated by " - "
                if len(type_dict_pair) == 2:
                    self.file_associations[type_dict_pair[0]] = type_dict_pair[1]
        f.close()

    # if a directory name in file_associations is not in the base_path directory, create it
    def update_child_directories(self):
        current_files = os.listdir(self.base_path)
        for dict_name in self.file_associations.values():
            if dict_name not in current_files:
                dir_path = os.path.join(self.base_path, dict_name)
                current_files.append(dict_name)
                os.mkdir(dir_path)
    
    # sort files into correct directories
    def sort_files(self):
        current_files = os.listdir(self.base_path)
        for file_name in current_files:
            if file_name not in self.file_associations.values():
                (file_ext, new_file_name) = self.resolve_file_name(file_name)
                old_path = os.path.join(self.base_path, file_name)
                new_path = os.path.join(self.base_path, self.file_associations[file_ext], new_file_name)
                os.rename(old_path, new_path)
    
    # get file extension and change file_name if corresponding directory has a file with the same name
    def resolve_file_name(self, file_name):
        split_name = file_name.split(".")
        # get the last element from file name separated by "."s to check extension
        file_ext = "." + split_name[-1]
        # if the extension is unknown, sort into other
        if file_ext not in self.file_associations:
            file_ext = "other"
        if os.path.isdir(os.path.join(self.base_path, file_name)):
            file_ext = "dir"
        files_in_dir = os.listdir(os.path.join(self.base_path, self.file_associations[file_ext]))
        i = 1
        split_name.insert(1, "")
        # add (i) to the file name, increasing i until a unique name is achieved
        while file_name in files_in_dir:
            split_name[1] = ("(" + str(i) + ")")
            file_name = "".join(split_name[0:2])
            if len(split_name) > 2:
                file_name += "." + ".".join(split_name[2:])
            i += 1
        return file_ext, file_name




    
            
