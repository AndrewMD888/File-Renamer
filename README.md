README last updated by Andrew Dulichan on May 30, 2019
------------------------------------------------------

# File-Renamer

This is a script to rename filenames within a directory to be Operating System friendly across multiple OSes. Meant to clean up filenames en masse. Written in Python 3. To run the program you can use an IDE or Python directly via the terminal on your computer.

The file naming convention I chose is based on generally accepted guidelines across systems. No special characters, spaces, capital letters, etc. Separate words with underscores, and hyphens are allowed to remain in lieu of underscores.

The main formatting character I chose to use for replacement is an underscore. It is the main separator character.

I use a somewhat heavy amount of regular expressions to achieve my goal.

For now, I've chosen to make this program relatively simplistic. I'm not going to try to cover every case of characters out there as the list is exhaustive. That can come later on.

I formulated this program in a specific way that might perform repetitive, unnecessary steps for certain strings. However, certain strings are tricky to deal with and all of these steps are necessary for those specific strings.

The main aspect of this program is that it relies upon certain conditions and occurrences in the filename string in order to work. Complex file names full of mish-mash characters won't turn out perfectly (although, who names their files like that anyway?). In short, the program cannot distinguish between actual words/natural language (which is a weakness of computers in general), so for now I don't expect this kind of thing to be perfect. I tried to code it so that it can recognize words decently.

Of course, this program is meant to clean up filenames, not provide brand new names for them. It cannot predict what a user wants their files to be called; it works with what it is given.

This project began as a way for me to get familiar with Python and regular expressions. It wasn't meant to be an exhaustive project, although it can certainly grow into that. If you have feedback and/or improvements for this program, let me know.

**TO-DO LIST**

1. Adjust program to append strings for the Regular Expression matches where necessary, not use replacement
2. Expand the dictionary rules as needed to cover more cases and remove more troublesome characters
3. Update to allow the user to rename one file and not just a whole directory. Make this program more efficient by cleaning up the regular expressions and seeing if anything can be removed/refactored
4. Probably update to allow the user to choose what sort of dictionary rules they want via a mode selector for this program's behavior (rules pre-defined by me)
