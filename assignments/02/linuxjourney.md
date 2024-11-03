# Linux Journey: Shell-Lektionen

This file contains the answers to the quiz questions and the output of the commands from the exercises for each of the 19 lessons on [Linux Journey - The Shell](https://linuxjourney.com/lesson/the-shell).


---
## **Quiz**
1. Hello World
2. `pwd`
3. `cd ..`
4. `ls -a`
5. `touch myfile`
6. `file`
7. `cat`
8. `q`
9. `clear`
10. `-r`
11. `mv cat dog`
12. `mkdir`
13. `rm myfile`
14. `-name`
15. `help`
16. `man`
17. `whatis`
18. `alias`
19. `exit`


## Tab 1: **[The Shell]**

### Exercises
**Task**: Try some other Linux commands and see what they output:
- $ date
    - Sun Nov  3 14:45:36     2024
- $ whoami
    - User1


## Tab 2: **[pwd (Print Working Directory)]**

### Exercises
No exercises for this lesson.


## Tab 3: **[cd (Change Directory)]**

### Exercises
**Task**: Run the cd command without any flags, where does it take you?:
**Answer**: Running `cd` without arguments takes you to your home directory.


## Tab 4: **ls (List Directories)**

### Exercises
**Task**: Run ls with different flags and see the output you receive.
- ls -R: recursively list directory contents
    - AboutMe.md  linuxjourney.md
- ls -r: reverse order while sorting
    - linuxjourney.md  AboutMe.md
- ls -t: sort by modification time, newest first
    - linuxjourney.md  AboutMe.md


## Tab 5: **touch**

### Exercises
**Task**: 
- Create a new file
    - touch Test.txt
- Note the timestamp
- Touch the file and check the timestamp once again


## Tab 6: **file**

### Exercises 
**Task**: Run the file command on a few different directories and files and note the output.
- file Test.txt


## Tab 7: **cat**

### Exercises
**Task**: Run cat on different files and directories. Then try to cat multiple files.
- cat


## Tab 8: **less**

### Exercises
**Task**: Run less on a file, then page up and around the file. Try searching for a specific word. Quickly navigate to the beginning or the end of the file.


## Tab 9: **history**

### Exercises
**Task**: Navigate through your previous command history with the Up and Down keys. Play around with ctrl-R reverse search.


## Tab 10: **cp (Copy)**

### Exercises
**Task**: Copy over a couple of files, be careful not to overwrite anything important.
- cp Test.txt


## Tab 11: **mv (Move)**

### Exercises
**Task**: Rename a file, then move that file to a different directory.
- mv Test.txt TEST.txt


## Tab 12: **mkdir (Make Directory)**

### Exercises
**Task**: Make a couple of directories and move some files into that directory.


## Tab 13: **rm (Remove)**

### Exercises
**Task**: 
- Create a file called -file (don't forget the dash!).
    - touch file.txt
- Remove that file.
    - rm file.txt


## Tab 14: **find**

### Exercises
**Task**: Find a file from the root directory that has the word net in it.


## Tab 15: **help**

### Exercises
**Task**: Run help on the echo command, logout command and pwd command.
- help echo
- help logout
- help pwd


## Tab 16: **man**

### Exercises
**Task**: Run the man command on the ls command.
```
$ man ls
bash: man: command not found
```

## Tab 17: **whatis**

### Exercises
**Task**: Run the whatis command on the less command.
```
$ whatis less
bash: whatis: command not found
```


## Tab 18: **alias**

### Exercises
**Task**: Create a couple of aliases then remove them.
- alias foobar='ls -la'
- unalias foobar


## Tab 19: **exit**

### Exercises
**Task**: Exit out of the shell and see what happens. Make sure you don't need to do anymore work in that shell.
- exit
