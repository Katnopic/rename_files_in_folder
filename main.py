import sys
import os

# Function that replaces string_to_remove from files in folder_path with with string_to_add
def replace_str_end_of_filename(folder_path,string_to_remove,string_to_add):

    # get all file names in folder 
    filenames = os.listdir(folder_path)
    
    # run on each file and replace string_to_remove with string_to_add
    for filename in filenames:

        # get absolute path to file
        abs_file_path = folder_path + filename
        
        try: 
            # rename the file
            os.rename(abs_file_path, abs_file_path.replace(string_to_remove,string_to_add))
        except:
            e = sys.exc_info[0]
            print "error renaming file: {}. error thrown by system: {}".format(abs_file_path,e)

    print "filenames in {} were sucesfully edited.".format(folder_path)

# Inputs
folder_path = raw_input("Enter path to folder: ")
string_to_remove = raw_input("enter string to remove at the end of the files: ")
string_to_add = raw_input("Enter string to replace the removed string: ")

# call function to replace certain string in filenames
replace_str_end_of_filename(folder_path,string_to_remove,string_to_add)

