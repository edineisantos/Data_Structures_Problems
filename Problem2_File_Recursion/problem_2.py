import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limits to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix of the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    # Check if path is None and return an empty list if true
    if path is None:
        print("Path is None. Please provide a valid path.")
        return []

    if not os.path.isdir(path):
        return []  # Return an empty list if the path is not a directory

    matched_files = []  # List to store all matched files' paths
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)  # Generate full path of the entry
        if os.path.isdir(full_path):
            # If entry is a directory, recursively search this directory
            matched_files.extend(find_files(suffix, full_path))
        elif os.path.isfile(full_path) and full_path.endswith(suffix):
            # If entry is a file and ends with the suffix, add it to the list
            matched_files.append(full_path)
    
    return matched_files

# Test Case 1: Searching in 'testdir' for '.c' files
print("Test Case 1: Searching in 'testdir' for '.c' files")
found_files = find_files('.c', './testdir')
if found_files:
    for file in found_files:
        print(file)
else:
    print("No files found.")
print("\n")

# Test Case 2: Attempting to search in a null directory path
print("Test Case 2: Attempting to search in a null directory path")
found_files = find_files('.c', None)
if not found_files:
    print("Handled null directory path correctly (no files found).")
else:
    print("Unexpected behavior with null directory path.")
print("\n")

# Test Case 3: Searching in an empty directory
print("Test Case 3: Searching in an empty directory")
# Check if 'emptydir' exists, if not, create it
empty_dir_path = './emptydir'
if not os.path.exists(empty_dir_path):
    os.makedirs(empty_dir_path)

# Run the find_files function to the empty directory
found_files = find_files('.c', empty_dir_path)
if not found_files:
    print("Correctly identified no files in an empty directory.")
else:
    print("Unexpected behavior with an empty directory.")
print("\n")
