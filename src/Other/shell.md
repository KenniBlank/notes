# Shell

```bash
pwd # current directory

ls /home/repl/surr # list all things with in the directory (absolute directory: starts with /)
ls # list items in current directory (relative directory)
ls -R # Shows every file and directory in current level and everything in sub directories
ls -F # prints / after the name of every directory and * after name of every runnable program

cd # move around in directories
cd ~/ # move to previous directory
cp file.txt ... /place
mv file.csv ... /place # can also be used to rename file and folders
rm filename.format # removes file
rmdir people/ # remove folder
mkdir ~/.yearly #create folder one directory back

cat file.txt # prints the content of the file

less file1.txt file2.txt
    # use :n to go to second file
    # :q to quit
    # SPACEBAR to page down

head /folder/file.txt #displays first 10 rows of the file
    # head -n 3 file.txt to display only 3 rows and so on...

# TO know what command does: use man short for manual probably
man tail # brings relevant info, auto invokes less
# One-line description
# summary under SYNOPSIS lists all flags it understands
# Everything optional in [...], either or separated by |
# things that can be repeated ...

cut -d, -f1 seasonal/spring.csv # gets first line from the file

history # provides history of recently run command
# !number selects the line with that number
# !commandName runs the latest commant starting with that command
```

**head** and **tail** select rows
**cut** selects columns

**grep** selects lines according to what they contain.
  -c: print a count of matching lines rather than the lines themselves
  -h: do not print the names of files when searching multiple files
  -i: ignore case (e.g., treat "Regression" and "regression" as matches)
  -l: print the names of files that contain matches, not the matches
  -n: print line numbers for matching lines
  -v: invert the match, i.e., only show lines that don't match
