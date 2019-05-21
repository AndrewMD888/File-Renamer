# Created by Andrew Dulichan on February 19, 2018, last updated by Andrew Dulichan on May 21, 2019
# SEE THE README IN MY REPOSITORY FOR DOCUMENTATION!

import os, re

#----------Start of function-----------------
def my_rename(file_name):

    # The blanket rules (find and replace cases) I came up with for how I want this program to function. Key-value pairs.
    dictionary_rules = {'"': '', "'": "", " ": "_", '`': '', "!": "", "@": "_at", "#": "", "$": "", "%": "", "^": "", "&": "_and", "|": "_or", "(": "", ")": "", "{": "", "}": "", "[": "", "]": ""}

    # Create the actual dictionary for usage on strings
    my_dictionary = dict((re.escape(k), v) for k, v in dictionary_rules.items())

    # Compiling the dictionary for usage with the .sub (search and replace) function
    pattern = re.compile("|".join(my_dictionary.keys()))
    
    # Search and replace action on the file_name string using the dictionary
    temp_string = pattern.sub(lambda m: my_dictionary[re.escape(m.group(0))], file_name)

    # Logic checks to see if the first group to match in the string is not alphanumeric
    # Program goes into this code block if the first character of the string is not alphanumeric
    if re.match(r'(^[A-Z]+)|(^[a-z]+)|(^[0-9]+)', temp_string) is None:
        
        # If a match was not found (not alphanumeric), remove the non alphanumeric characters from the start of the string
        start_of_string_trimmed = re.sub(r'^[^A-Za-z0-9]+', r'', temp_string)

        print(start_of_string_trimmed)

        # I chose 2 or more capital letters to match for below because this excludes first character capitalization, which is what I want here
        temp_string2 = re.sub(r'(^[A-Z]{2,})', r'\1_', start_of_string_trimmed)

        print(temp_string2)

        # Inserts an underscore after the capturing group only if there are two or more consecutive lowercase letters in that group
        # Done so that the formatting of version numbers (for example, v1.03.54) is left as is
        temp_string3 = re.sub(r'((?<![A-Za-z\.])[a-z]{2,}(?=[a-z]*))', r'\1_', temp_string2)

        print(temp_string3)

        temp_string4 = re.sub(r'((?<![A-Za-z])[0-9](?=[A-Za-z]))', r'\1_', temp_string3)

        print(temp_string4)

        # Inserts an underscore after a sequence of 2 or more characters and before a number
        temp_string5 = re.sub(r'((?<![0-9])[A-Za-z]{2,}(?=[0-9]))', r'\1_', temp_string4)

        print(temp_string5)

        # Gets the first character of the string for later usage
        save = re.search(r'(^[A-Z0-9]+)|(^[a-z0-9]+)', temp_string5).group()

        # temp_string6 is not used in this conditional branch
        # As such, I initialized temp_string6 to an empty list of two elements to avoid an exception in later conditional statements
        # Hardcoding works here due to those statement's conditions
        temp_string6 = [None] * 2

        # Converts the first character of the string to lowercase for replacement in the string later on
        start_of_string_formatter = str(save).lower()

    # This code branch is used if the first character of the string is alphanumeric
    else:

        # I chose 2 or more capital letters to match for below because this excludes first character capitalization, which I want excluded here
        temp_string2 = re.sub(r'(^[A-Z]{2,})', r'\1_', temp_string)

        print(temp_string2)

        # Gets the first character of the string for later usage
        save = re.search(r'(^[A-Z0-9]+)|(^[a-z0-9]+)', temp_string2).group()

        # Inserts an underscore after the capturing group only if there are two or more consecutive lowercase letters in that group
        # Done so that the formatting of version numbers (for example, v1.03.54) is left as is
        temp_string3 = re.sub(r'((?<![A-Za-z\.])[a-z]{2,}(?=[a-z]*))', r'\1_', temp_string2)

        print(temp_string3)

        temp_string4 = re.sub(r'((?<![A-Za-z])[0-9](?=[A-Za-z]))', r'\1_', temp_string3)

        print(temp_string4)

        # Inserts an underscore after a sequence of 2 or more characters and before a number
        temp_string5 = re.sub(r'((?<![0-9])[A-Za-z]{2,}(?=[0-9]))', r'\1_', temp_string4)

        print(temp_string5)

        # temp_string6 is now populated and is the same value as temp_string5
        temp_string6 = temp_string5

        # Converts the first character of the string to lowercase for replacement in the string later on
        start_of_string_formatter = str(save).lower()

    # Checking to see temp_string5 and temp_string6 have certain characters in the second position
    if temp_string5[1] == "_" and temp_string6[1] != "_":

        # Removes underscores where necessary
        temp_string6 = re.sub(r'((?<=[A-Za-z0-9_])[_]+(?![A-Za-z0-9]))', r'', temp_string5)

        print(temp_string6)

        # Appends an underscore into the correct place for capturing group 2 after removing prior undesirable underscores
        temp_string7 = re.sub(r'((?<!^[a-z0-9])[_](?![A-Z0-9_]))|((?<!^[A-Z0-9])[_](?![a-z0-9][_]))', r'\2_', temp_string6)

        print(temp_string7)
    
    elif temp_string6[1] == "_":

        # Removes underscores where necessary
        temp_string6 = re.sub(r'((?<=[A-Za-z0-9_])[_]+(?![A-Za-z0-9]))', r'', temp_string5)

        print(temp_string6)

        # Appends an underscore into the correct place after removing prior undesirable underscores
        temp_string7 = re.sub(r'((?<!^[a-z0-9])[_](?![A-Z0-9_]))|((?<!^[A-Z0-9])[_](?![a-z0-9][_]))', r'\2_', temp_string6)

        print(temp_string7)

    else:

        # If everything was fine, we don't need temp_string6 and can put temp_string5's value directly into temp_string7 for the next steps
        temp_string7 = temp_string5

    # The first character of the string in lowercase now replaces whatever character is in the first position at this point
    temp_string8 = re.sub(r'(^[A-Z]+)|(^([A-Z]+)([a-z]+\.))', start_of_string_formatter, temp_string7)
    
    print(temp_string8)

    # Inserts underscores between lowercase letters and capital words properly
    # The "r'\1\2_'" syntax is the proper way to add an underscore after capturing group 1 and 2
    temp_string9 = re.sub(r'([a-z](?=[A-Z]))|([A-Z]{2,}(?=[a-z]))', r'\1\2_', temp_string8).lower()

    print(temp_string9)

    # Removes any remaining extraneous/unnecessary underscores from the entire string
    temp_string10 = re.sub(r'((?<=[a-z])[_]+(?=[\.]))|((?<=[0-9])[_]+(?=[\.]))|((?<![a-z0-9])[_](?![A-Z]))', r'', temp_string9)

    print(temp_string10)

    # Removes any amount of underscores on either side of a hyphen to avoid multiple consecutive separator characters
    final_string = re.sub(r'([_]{1,}(?=[-]))|((?<=[-])[_]{1,})', r'', temp_string10)

    print(final_string)

    return final_string

#----------End of function-------------------

# The print statements in the script are for user-friendliness 
# The print statements' logic in the script relies upon a comparison between the old and new filename
# The script will execute successfully even if the file wasn't technically renamed (due to it not meeting one of the rules from the above function)
# This means we have to write the code properly to print the messages we want properly

#-----------Start of script------------------
directory = input("Enter the directory path in which you wish to have all filenames changed: ")

# Loops through the files in a directory and if files are found, they are added to a variable
# Then len() returns how many files were found in that variable, as an integer
num_files_in_directory = len([files for files in os.listdir(directory) if os.path.isfile(os.path.join(directory, files))])
directory_files = os.listdir(directory)

# Error message if no files are found
if not directory_files:

    print("\nYou entered a directory which has no files in it. Restart the program and try again.")

else:

    renamed_file_counter = 0
    non_renamed_file_counter = 0

    for filename in directory_files:

        # Save original filename for later comparison
        original_filename = filename

        # Get the new filename according to what my_rename() specified
        new_filename = my_rename(filename)

        # This line actually actions the file renaming
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

        if original_filename == new_filename:

            non_renamed_file_counter += 1

        if original_filename == new_filename and num_files_in_directory == 1:

            print("\nThe lone file named " + original_filename + " in the specified directory was not renamed, as this script was unnecessary for that file.")
            break

        elif original_filename != new_filename:

            print("\n" + original_filename + " has been renamed to " + new_filename)
            
        renamed_file_counter += 1

    if (original_filename != new_filename and renamed_file_counter >= 1) or renamed_file_counter > non_renamed_file_counter:

       print("\n" + str(renamed_file_counter - non_renamed_file_counter) + " file(s) renamed.")

    if non_renamed_file_counter >= 1 and num_files_in_directory > 1:

       print("\n" + str(non_renamed_file_counter) + " file(s) in the specified directory were not renamed, as this script was unnecessary for them.")
#-----------End of script--------------------
