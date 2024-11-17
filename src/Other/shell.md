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

Examples:
```bash
grep molar file.txt # outputs all the lines with molar in it
grep molar -v file.txt # outputs all the lines without molar in it
grep -c molar /seasonal/winter.csv /seasonal/autumn.csv # outputs the count of molar in each files
```


## Storing the command's output in a file:
```bash
(command) > file.xyz
```

## Pipe
This is very useful for combining commands.
```bash
head seasonals.csv | tail -n 2 # displays last two rows from the top 10 of the file

cut -d , -f 2 seas.csv | grep Tooth -V
# displays all values after the first ',' excluding the rows with 'Tooth
```


- wc (short for "word count")
```bash
grep 2017-07 file.txt | wc -l
# prints the count of lines of output of grep ...
```

- Many files at ounce

The terminal can handle all regular expressions
  - ? matches a single character, so 201?.txt will match 2017.txt or 2018.txt, but not 2017-01.txt.
  - [...] matches any one of the characters inside the square brackets, so 201[78].txt matches 2017.txt or 2018.txt, but not 2016.txt.
  - {...} matches any of the comma-separated patterns inside the curly brackets, so {*.txt, *.csv} matches any file whose name ends with .txt or .csv, but not files whose names end with .pdf.
```bash
head -n 3 seasonal/s*.csv
# outputs first 3 lines of all files beginning with s and ending with .csv
```


- sort (puts data in order, default is ascending)
  - f :case insensitive
  - n :sort numerically
  - r :reverse sort order of ouptu
  - b :ignore leading blank

  > Piping sort -n to head shows you the largest values

- uniq (remove duplicate lines: removes *adjacent* duplicated lines)
  - c (count of how many times the line repeated)

- wc (word count)


## Storing Information in the Shell
Like all programs, shell stores information in variables. Some of these, called **environment variables**, are available all the time.

Varible, Purpose, Value

- HOME, User's home directory, /home/repl
- PWN, Present working directory, same as pwd command
- SHELL, which shell program is being used, /bin/bash
- USER, User's ID, repl

To get complete list, type **set** in the shell.

Printing variable's value:

- **echo**

```bash
echo hello world
echo USER # print the variable name, USER
echo $USER # prints 'repl' which is the variable's value
```


The Other kind of variable is called a shell variable (basically local variable)
```bash
train=xyz.csv   # no space, no type
echo $train     # prints xyz.csv
```


## Repeating a command multiple times:

Loops:
```bash
for filetype in gif jpg png; do echo $filetype; done
# Output:
# gif
# jpg
# png
```
```bash
for filename in people/*;
do echo $filename;
done

# Outputs name of all file inside of people
```

## Beauty of the Shell Script
The extension of bash script doesn't have to be .sh but its the convention
```bash
bash *.sh
# runs all bash script in the current directory
```

How to pass filenames to shell script?
```bash
# shell script
sort $@ | uniq

# Running the shell script
bash nameOfScript.sh file.txt

# sorts and outputs the content of the file...
```

Another way
```bash
# $1 $2 ... to speciy command-line parameters
cut -d, -f $2 $1

# Running the script
bash script.sh x.csv 1
```
