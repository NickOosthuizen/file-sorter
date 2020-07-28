# File Sorter

This program sorts files by extension in a specified directory into 
directories specified by the user.

## Getting Started

Pull project from Github. The text file "associations.txt" must be
edited before use. The top line needs to be the path of the directory
that needs sorting, and following lines need to be of the form:
    .extension - directory
where .extension is a file extension and directory is the name of 
the directory for this extension to go into. The sorter creates a 
directory for unrecognized file extensions and for directories by 
default. To change the names of these directories, add "other" 
and/or "dir" to the text file in the same form as for other 
extensions.

### Prerequiestes

Python is required to run