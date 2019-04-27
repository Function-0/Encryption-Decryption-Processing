# Constant: Select the python file handle that will have its trailing 
# whitespace removed
PYTHON_FILE_HANDLE = "cipher_functions.py"
# Retrieve the file handle 
python_file_handle_copy = open(PYTHON_FILE_HANDLE, 'r')
# Obtain all file data within the given file handle
python_file_data_copy = python_file_handle_copy.readlines()
# Close the given file handle
python_file_handle_copy.close()
# Create a new file to write the new file data with trailing whitespace removed
# Said file will be the original file in write mode
fixed_python_file = open(PYTHON_FILE_HANDLE, 'w')
# Elemental loop: Go through each line in the given file data
for line in python_file_data_copy:
    # Strip the line from the right side (right-justification)
    line_fixed = line.rstrip()
    # Write the line into the new file 
    fixed_python_file.write(line_fixed + "\n")
# Close the new file handle
fixed_python_file.close()

