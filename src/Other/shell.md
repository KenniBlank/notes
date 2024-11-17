# Shell Command Reference
## Basic Navigation and File Management
```bash
pwd                     # Print current directory
ls                      # List items in current directory
ls /path/to/dir        # List items in specified directory
ls -R                   # List all files and directories recursively
ls -F                   # Append / for directories and * for executables

cd /path/to/dir        # Change to specified directory
cd ~                    # Change to home directory
cd ..                   # Move up one directory

cp source.txt dest.txt  # Copy file
mv oldname.txt newname.txt # Move or rename file
rm filename.txt         # Remove file
rmdir directory          # Remove empty directory
mkdir new_directory      # Create new directory
```

## File Viewing and Manipulation
```bash
cat file.txt            # Display file content
less file1.txt          # View file with pagination
head file.txt           # Display first 10 lines
head -n 5 file.txt      # Display first 5 lines

# Use man for command manual
man command_name        # Display manual for command
```

## Text Processing
```bash
cut -d, -f1 file.csv    # Extract first column from CSV
grep pattern file.txt    # Search for pattern in file
grep -c pattern file.txt  # Count matching lines
grep -v pattern file.txt  # Show lines that do not match

# Pipe example
head file.txt | tail -n 2  # Display last 2 lines of the first 10
```

## Output Redirection and Piping
```bash
command > output.txt      # Redirect output to file
command1 | command2       # Pipe output of command1 to command2
```

## Word Count and Sorting
```bash
wc -l file.txt            # Count lines in file
sort file.txt             # Sort file content
sort -n file.txt          # Sort numerically
uniq file.txt             # Remove duplicate lines
```

## Variables
```bash
echo $USER                # Print value of USER variable
my_var=value              # Define a shell variable
echo $my_var              # Print variable value
```

## Loops
```bash
for filetype in gif jpg png; do
    echo $filetype
done

for filename in directory/*; do
    echo $filename
done
```

## Shell Scripts
```bash
bash script.sh            # Run a shell script
sort $@ | uniq            # Sort and remove duplicates from input files
cut -d, -f $2 $1         # Use command-line parameters in script
```

## Regular Expressions
- **?** matches a single character
- **[...]** matches any character in brackets
- **{...}** matches any of the comma-separated patterns
```bash
#!/bin/bash

# Create sample files
touch file1.txt file2.txt file3.csv file4.txt file5.csv file6.doc

# Display all files
echo "All files:"
ls

# Use regular expressions to match files
echo -e "\nFiles that start with 'file' and end with '.txt':"
ls file*.txt

echo -e "\nFiles that start with 'file' and have a single character before '.csv':"
ls file?.csv

echo -e "\nFiles that are either .txt or .csv:"
ls file{1..5}.{txt,csv}

# Use grep to filter content in a sample text file
echo -e "\nCreating a sample text file for grep demonstration..."
echo -e "apple\nbanana\ncherry\napricot\nblueberry" > fruits.txt

echo -e "\nLines containing 'a' or 'b':"
grep '[ab]' fruits.txt

echo -e "\nLines that do not contain 'a':"
grep -v 'a' fruits.txt

# Clean up
rm file*.txt file*.csv file*.doc fruits.txt
```
