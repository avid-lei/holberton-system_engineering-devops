# 0x00. Shell, basics

## Description
What you should learn from this project:

* What does RTFM mean?
* What is a Shebang

---

### [0. Where am I?](./0-current_working_directory)
* Write a script that prints the absolute path name of the current working directory.


### [1. Who am I](./1-who_am_i)
* Write a script that prints the effective userid of the current user.


### [2. Groups](./2-groups)
* Write a script that prints all the groups the current user is part of.


### [3. New owner](./3-new_owner )
* Write a script that changes the owner of the file hello to the user betty.


### [4. Empty!](./4-empty)
* Write a script that creates an empty file called hello.


### [5. Execute](./5-execute)
* Write a script that adds execute permission to the owner of the file hello.


### [6. Multiple permissions](./6-multiple_permissions)
* Write a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.


### [7. Everybody!](./7-everybody)
* Write a script that adds execution permission to the owner, the group owner and the other users, to the file hello


### [8. James Bond](./8-James_Bond)
* Write a script that sets the permission to the file hello as follows:


### [9. John Doe](./9-John_Doe)
* Write a script that sets the mode of the file hello to this:


### [10. Look in the mirror](./10-mirror_permissions)
* Write a script that sets the mode of the file hello the same as olleh’s mode.


### [11. Directories](./11-directories_permissions)
* Create a script that adds execute permission to all subdirectories of the current directory for  the owner, the group owner and all other users. Regular files should not be changed.


### [12. More directories](./12-directory_permissions)
* Create a script that creates a directory called dir_holberton with permissions 751 in the working directory.


### [13. Change group](./13-change_group)
* Write a script that changes the group owner to holberton for the file hello


### [14. Owner and group](./14-change_owner_and_group)
* Write a script that changes the owner to betty and the group owner to holberton for all the files and directories in the working directory.


### [15. Symbolic links](./15-symbolic_link_permissions)
* Write a script that changes the owner and the group owner of the file _hello to betty and holberton respectively.
### [16. If only](./16-if_only )
* Write a script that changes the owner of the file hello to betty only if it is owned by the user guillaume.
### [17. Star Wars](./100-Star_Wars)
* Write a script that will play the StarWars IV episode in the terminal.
### [18. RTFM](./101-man_holberton)
* Create a man page that looks exactly like this one and passes all checks.
---
## Author
vagrant@vagrant-ubuntu-trusty-64:~/holberton-system_engineering-devops/0x01-shell_permissions$ vagrant@vagrant-ubuntu-trusty-64:~/holberton-system_engineering-devops/0x01-shell_permissions$ vagrant@vagrant-ubuntu-trusty-64:~/holberton-system_engineering-devops/0x01-shell_permissions$ cat README.md
# 0x01. Shell, permissions
## Description
What you should learn from this project:
* What do the commands chmod, sudo, su, chown, chgrp do
* Linux file permissions
* How to represent each of the three sets of permissions (owner, group, and other) as a single digit
* How to change permissions, owner and group of a file
* Why can’t a normal user chown a file
* How to run a command with root privileges
* How to change user ID or become superuser
---
### [0. My name is Betty](./0-iam_betty)
* Create a script that changes your user ID to betty.
### [1. What’s in there?](./1-listit)
* Write a script that displays the contents list of your current directory.
### [2. There is no place like home](./2-bring_me_home)
* Write a script that changes the working directory to the user’s home directory.
### [3. The long format](./3-listfiles )
* Write a script that displays current directory contents in a long forma.
### [4. Hidden files](./4-listmorefiles)
* Write a script that displays current directory contents, including hidden files (starting with .). Use the long format.
### [5. I love numbers ](./5-listfilesdigitonly)
* Write a script that displays current directory contents in long format, with user and group IDs displayed numerically and hidden files (starting with .).
### [6. Welcome holberton](./6-firstdirectory)
* Write a script that creates a directory named holberton in the /tmp/ directory.
### [7. Betty in Holberton](./7-movethatfile)
* Write a script that moves the file betty from /tmp/ to /tmp/holberton.
### [8. Bye bye Betty](./8-firstdelete)
* Write a script that deletes the file betty.:
### [9. Bye bye Holberton](./9-firstdirdeletion)
* Write a script that deletes the directory holberton that is in the /tmp directory.:
### [10. Back to the future](./10-back)
* Write a script that changes the working directory to the previous one.
### [11. Lists](./11-lists)
* Create a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.
### [12. File type](./12-file_type)
* Write a script that prints the type of the file named iamafile. The file iamafile will be in the /tmp directory when we will run your script.
### [13. We are symbols, and inhabit symbols](./13-symbolic_link)
* Create a symbolic link to /bin/ls, named __ls__. The symbolic link should be created in the current working directory.

### [14. Copy HTML files](./14-copy_html)
* Create a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.


### [15.  Let’s move](./15-lets_move)
* Create a script that moves all files beginning with an uppercase letter to the directory /tmp/u.


### [16. Clean Emacs](./16-clean_emacs )
* Create a script that deletes all files in the current working directory that end with the character ~.


### [17. Tree](./17-tree)
* Create a script that creates the directories welcome/, welcome/to/ and welcome/to/holberton in the current directory.


### [18. Life is a series of commas, not periods](./18-commas)
* Write a command that lists all the files and directories of the current directory, separated by commas (,).

### [19. File type: Holberton](./holberton.mgc)
* Create a magic file holberton.mgc that can be used with the command file to detect Holberton data files. Holberton data files always contain the string HOLBERTON at offset 0.
---

## Author
* **Diva Lei** - [lei-diva](https://github.com/lei-diva)
