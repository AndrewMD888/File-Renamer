#!/usr/bin/python3
# -*- coding: utf-8 -*-

# First created on February 19, 2018. Last updated on May 14, 2021.
# SEE THE README IN THE REPOSITORY FOR DOCUMENTATION

# This program is currently not compatible with Python 2, so line 1 ensures the user uses Python 3 if running via the terminal
# I specified the encoding set for this file, just in case

import os, re

#------------Start of filename conversion function-------------
#--------------------------------------------------------------

def filename_conversion(filename):
    # The blanket rules (find and replace cases) I came up with for how I want this program to function. Key-value pairs.
    dictionary_rules = {'"': '', "'": "", " ": "_", '`': '', "!": "", ";": "", "–": "-", "@": "_at", "#": "", "$": "", "%": "", "^": "", "&": "_and", "|": "_or", "(": "", ")": "", "{": "", "}": "", "[": "", "]": ""}

    # Create the actual dictionary for usage on filenames
    filename_dictionary = dict((re.escape(key), value) for key, value in dictionary_rules.items())

    # Compiling the dictionary for usage with the .sub (search and replace) function
    pattern = re.compile("|".join(filename_dictionary.keys()))
    
    # Search and replace action on the filename string using the dictionary
    filename_to_rename_pass1 = pattern.sub(lambda m: filename_dictionary[re.escape(m.group(0))], filename)

    # Logic checks to see if the first group to match in the string is not alphanumeric
    # Program goes into this code block if the first character of the string is not alphanumeric
    if re.match(r'(^[A-Z]+)|(^[a-z]+)|(^[0-9]+)', filename_to_rename_pass1) is None:
        # If a match was not found (not alphanumeric), remove the non alphanumeric characters from the start of the string
        start_of_filename_trimmed = re.sub(r'^[^A-Za-z0-9]+', r'', filename_to_rename_pass1)

        # I chose 2 or more capital letters to match for below because this excludes first character capitalization, which is what I want here
        filename_to_rename_pass2 = re.sub(r'(^[A-Z]{2,})', r'\1_', start_of_filename_trimmed)

        # Inserts an underscore after the capturing group only if there are two or more consecutive lowercase letters in that group
        # Done so that the formatting of version numbers (for example, v1.03.54) is left as is
        filename_to_rename_pass2 = re.sub(r'((?<![A-Za-z\.])[a-z]{2,}(?=[a-z]*))', r'\1_', filename_to_rename_pass2)

        filename_to_rename_pass2 = re.sub(r'((?<![A-Za-z])[0-9](?=[A-Za-z]))', r'\1_', filename_to_rename_pass2)

        # Inserts an underscore after a sequence of 2 or more characters and before a number
        filename_to_rename_pass2 = re.sub(r'((?<![0-9])[A-Za-z]{2,}(?=[0-9]))', r'\1_', filename_to_rename_pass2)

        # Gets the first character of the string for later usage
        first_char_in_filename = re.search(r'(^[A-Z0-9]+)|(^[a-z0-9]+)', filename_to_rename_pass2).group()

        # filename_to_rename_pass3 is not used in this conditional branch
        # As such, I initialized filename_to_rename_pass3 to an empty list of two elements to avoid an exception in later conditional statements
        # Hardcoding works here due to those statement's conditions
        filename_to_rename_pass3 = [None] * 2

        # Converts the first character of the string to lowercase for replacement in the string later on
        start_of_filename_formatter = str(first_char_in_filename).lower()

    # This code branch is used if the first character of the string is alphanumeric
    else:
        # I chose 2 or more capital letters to match for below because this excludes first character capitalization, which I want excluded here
        filename_to_rename_pass2 = re.sub(r'(^[A-Z]{2,})', r'\1_', filename_to_rename_pass1)

        # Gets the first character of the string for later usage
        first_char_in_filename = re.search(r'(^[A-Z0-9]+)|(^[a-z0-9]+)', filename_to_rename_pass2).group()

        # Inserts an underscore after the capturing group only if there are two or more consecutive lowercase letters in that group
        # Done so that the formatting of version numbers (for example, v1.03.54) is left as is
        filename_to_rename_pass2 = re.sub(r'((?<![A-Za-z\.])[a-z]{2,}(?=[a-z]*))', r'\1_', filename_to_rename_pass2)

        filename_to_rename_pass2 = re.sub(r'((?<![A-Za-z])[0-9](?=[A-Za-z]))', r'\1_', filename_to_rename_pass2)

        # Inserts an underscore after a sequence of 2 or more characters and before a number
        filename_to_rename_pass2 = re.sub(r'((?<![0-9])[A-Za-z]{2,}(?=[0-9]))', r'\1_', filename_to_rename_pass2)

        # filename_to_rename_pass3 is now populated and is the same value as filename_to_rename_pass2
        filename_to_rename_pass3 = filename_to_rename_pass2

        # Converts the first character of the string to lowercase for replacement in the string later on
        start_of_filename_formatter = str(first_char_in_filename).lower()

    # Checking to see if filename_to_rename_pass2 and filename_to_rename_pass3 have certain characters in the second position
    if filename_to_rename_pass2[1] == "_" and filename_to_rename_pass3[1] != "_":
        # Removes underscores where necessary
        filename_to_rename_pass3 = re.sub(r'((?<=[A-Za-z0-9_])[_]+(?![A-Za-z0-9]))', r'', filename_to_rename_pass2)

        # Appends an underscore into the correct place for capturing group 2 after removing prior undesirable underscores
        filename_to_rename_final = re.sub(r'((?<!^[a-z0-9])[_](?![A-Z0-9_]))|((?<!^[A-Z0-9])[_](?![a-z0-9][_]))', r'\2_', filename_to_rename_pass3)
    
    elif filename_to_rename_pass3[1] == "_":
        # Removes underscores where necessary
        filename_to_rename_pass3 = re.sub(r'((?<=[A-Za-z0-9_])[_]+(?![A-Za-z0-9]))', r'', filename_to_rename_pass2)

        # Appends an underscore into the correct place after removing prior undesirable underscores
        filename_to_rename_final = re.sub(r'((?<!^[a-z0-9])[_](?![A-Z0-9_]))|((?<!^[A-Z0-9])[_](?![a-z0-9][_]))', r'\2_', filename_to_rename_pass3)

    else:
        # If everything was fine, we don't need filename_to_rename_pass3 and can put filename_to_rename_pass2's value directly into filename_to_rename_final for the next steps
        filename_to_rename_final = filename_to_rename_pass2

    # The first character of the string in lowercase now replaces whatever character is in the first position at this point
    filename_to_rename_final = re.sub(r'(^[A-Z]+)|(^([A-Z]+)([a-z]+\.))', start_of_filename_formatter, filename_to_rename_final)

    # Inserts underscores between lowercase letters and capital words properly
    # The "r'\1\2_'" syntax is the proper way to add an underscore after capturing group 1 and 2
    filename_to_rename_final = re.sub(r'([a-z](?=[A-Z]))|([A-Z]{2,}(?=[a-z]))', r'\1\2_', filename_to_rename_final).lower()

    # Removes any remaining extraneous/unnecessary underscores from the entire string
    filename_to_rename_final = re.sub(r'((?<=[a-z])[_]+(?=[\.]))|((?<=[0-9])[_]+(?=[\.]))|((?<![a-z0-9])[_](?![A-Z]))', r'', filename_to_rename_final)

    # Removes any amount of underscores on either side of a hyphen to avoid multiple consecutive separator characters
    filename_to_rename_final = re.sub(r'([_]{1,}(?=[-]))|((?<=[-])[_]{1,})', r'', filename_to_rename_final)

    return filename_to_rename_final

#--------------------------------------------------------------
#-------------End of filename conversion function--------------

#-----------------Start of renaming function-------------------
#--------------------------------------------------------------

# The print statements in this function are for user-friendliness 
# The print statements' logic in the function relies upon a comparison between the old and new filename
# The function will execute successfully even if the file wasn't technically renamed (due to it not meeting one of the rules from filename_conversion())
# This means we have to write the code properly to print the messages we want properly

def rename_files(directory):
    # Exception handling for the case where the user inputs an invalid directory
    try:
        # Loops through the files in a directory and if files are found, they are added to a variable
        # Then len() returns how many files were found in that variable, as an integer
        num_files_in_directory = len([files for files in os.listdir(directory) if os.path.isfile(os.path.join(directory, files))])
        directory_files = os.listdir(directory)
    except FileNotFoundError:
        print("\nYou entered a non-existent directory. Restart the program and try again.\n")
        return

    # Error message if no files are found
    if not directory_files:
        print("\nYou entered a directory which has no files in it. Restart the program and try again.\n")

    else:
        renamed_file_counter = 0
        non_renamed_file_counter = 0
        filename_collision_counter = 1 # Offset to 1 to properly sync with the amount of filenames that collide
        suffix = "_copy_"
        suffix_counter = 1 # Start at 1 for better user-readability

        for original_filename in directory_files:
            # Get the new filename according to what filename_conversion() specified
            new_filename = filename_conversion(original_filename)

            #---------Start of filename collision checking code----------

            # Filename collision can happen when certain characters get stripped from the original filename(s) and multiple files then end up with the same name
            # This isn't allowed by the operating system and will cause a script error, so we need to check for this case and update the filenames appropriately if needed

            # Get the base filename and file extension of new_filename stored separately for later usage
            root, ext = os.path.splitext(new_filename)

            # Indefinite loop to keep trying to action the file renaming until it safely succeeds
            # Once it succeeds, we break out of the loop and move on to the next file
            # Allowing the FileExistsError to occur and handling it properly is an elegant solution for this problem
            while True:
                try:
                    # This line actually actions the file renaming
                    os.rename(os.path.join(directory, original_filename), os.path.join(directory, new_filename))
                    break
                except FileExistsError:
                    # If filenames collided, keep track of how many have the same name
                    filename_collision_counter += 1
                    # Make the new_filename contain the base filename, suffix, incremental counter and file extension. This finalizes the filename
                    new_filename = root + suffix + str(suffix_counter) + ext
                    suffix_counter += 1

            #----------End of filename collision checking code-----------

            if original_filename == new_filename:
                non_renamed_file_counter += 1

            if original_filename == new_filename and num_files_in_directory == 1:
                print("\nThe lone file named " + original_filename + " in the specified directory was not renamed, as this script was unnecessary for that file.\n")
                break

            elif original_filename != new_filename:
                print("\n" + original_filename + " has been renamed to " + new_filename)
            
            renamed_file_counter += 1

        # Let the user know if filename collision occurred, and how it was mitigated if so
        if filename_collision_counter > 1:
            print("\nThe renaming process resulted in " + str(filename_collision_counter) + " files having the same name. An incremental suffix has been added to the necessary filenames to avoid errors.")

        if (original_filename != new_filename and renamed_file_counter >= 1) or renamed_file_counter > non_renamed_file_counter:
            print("\n" + str(renamed_file_counter - non_renamed_file_counter) + " file(s) renamed.")

        if non_renamed_file_counter >= 1 and num_files_in_directory > 1:
            print("\n" + str(non_renamed_file_counter) + " file(s) in the specified directory were not renamed, as this script was unnecessary for them.\n")

#--------------------------------------------------------------
#------------------End of renaming function--------------------

def _main():
    directory = input("Enter the full directory path in which you wish to have all files renamed: ")
    rename_files(directory)

# This lets the user import this program and use its functions as a module, instead of using the program as a script
# However, they still can use this program as a standalone script with this conditional statement
if __name__ == "__main__":
    _main()
