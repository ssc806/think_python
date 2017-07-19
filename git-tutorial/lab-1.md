# Lab 1

In this lab you will do the following:
* Configure Git
* Learn the Basic Commands of Git

## Prerequisites
For this lab you will need:
* A Cloud 9 Workspace

## Tasks

### Install Git

#### Determine if Git is installed
Since you are using a C9 workspace, Git should already be installed. You can verify this with the following command:

```console
$ git --version
```

You may be doing this outside of C9 though so if you do not get a response like the following:

`git version 2.10.2`

You should proceed to the [git-scm](https://git-scm.com/) site for download links and installation instruction. 
> Note: You may not get the exact version listed above. Any version of `git` will work for this lab.

#### Configuring Git

Now that we have veried that Git is installed, let's get it configured and ready to use. Git requires that a few config items are set before utilizing it. It needs to know who you are so it can include that information along with your work.
> Note: This will need to be done each time you create a new workspace. Luckily, it is quick and easy!

#### Set Your Email Address
Git requires that you set an email address in order to commit your work.  It won't verify that it is a correct email address, nor will it verify that it is your email address.  This information will be sent with your repo to anyone who collaborates with you on this repository.

```console
$ git config --global user.email "student@coder.education"
```
#### Set Your Real Name
Like your email address, Git wants to know your real name.  You can put whatever you want in here, but it will be shown along with your commits so be mindful of others when setting this.

```console
$ git config --global user.name "Student Coder"
```

### Create Your First Repsitory
The first step in working with Git is creating a repository. In order for Git to track your changes, it has to know where and what it is tracking. The repository is where Git stores all its information about the history and working contents of your directory.
> Note: Later we will learn how to collaborate with others and use existing repositories.

Create a directory for your repository and change to that directory:

```console
$ mkdir my_repo
$ cd my_repo
```

Create and initialize the Git repository in your new directory:
```console
$ git init .
Initialized empty Git repository in my_first_repo/.git
```

Now you have a repository ready to accept all your changes and keep track of your work.  You will notice that there is a `.git` directory in the current directory.  This is where Git stores all of the information it needs to keep track of your changes.

### Add a File to the Repository
First, let's create a file to add to our repository:
```console
$ echo "Hello World" > hello_world.txt
```

Now, add it to the repository:
```console
$ git add hello_world.txt
```

Finally, we commit the addition of the file:
```console
$ git commit -m 'Sometimes the world needs a "Hello".'
[master (root-commit) 5df0615] Added a very informative first file
 1 file changed, 1 insertion(+)
 create mode 100644 hello_world.txt
```

### Take a Look at the History of the Repository
Now that we have some history in Git, let's take a look:
```console
$ git log
commit 5df0615895e593a7c2b29f0dd802ca053fb72993
Author: Student Coder <student@coder.education>
Date:   Thu Aug 13 11:47:00 2015 -0500

    Sometimes the world needs a "Hello"
```

### Check the Status of Things
Since Git is managing the state of our directory for us we can ask it for a status at any time.
```console
$ git status
On branch master
nothing to commit, working directory clean
```

Let's add a file and see what Git tells us about the status.
```console
$ echo "Goodbye world" > goodbye_world.txt
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)

	goodbye_world.txt

nothing added to commit but untracked files present (use "git add" to track)
```

Add our new file and check the status.
```console
$ git add goodbye_world.txt
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   goodbye_world.txt
```

Now commit the file and check status.
```console
$ git commit -m "added a morbid file"
[master 38ef982] added a morbid file
 1 file changed, 1 insertion(+)
 create mode 100644 goodbye_world.txt

$ git status
On branch master
nothing to commit, working directory clean
```
Life is back to normal again!

### Change an Existing File
Let's say we want to change the contents of an existing file in our repository.  Change the contents of the `hello_world.txt` file.
```console
$ echo "Changed my mind" > hello_world.txt
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   hello_world.txt

no changes added to commit (use "git add" and/or "git commit -a")
```

Add those changes to our staged changes and commit.
```console
$ git add hello_world.txt
$ git commit -m "more insight to the world added"
[master 62e75d3] more insight to the world added
 1 file changed, 1 insertion(+), 1 deletion(-)
```

### Look At a Useful History
Now that we've done some things in our repository, let's look at a more interesting log of history.
```console
$ git log
commit 62e75d3a7e0a253a7ad71aa2e1581be04ae226a3
Author: Student Coder <student@coder.education>
Date:   Thu Aug 13 13:03:23 2015 -0500

    more insight to the world added

commit 38ef98238b4f35d85d1ea6a7333437723b21c7d0
Author: Student Coder <student@coder.education>
Date:   Thu Aug 13 12:56:10 2015 -0500

    added a morbid file

commit 5df0615895e593a7c2b29f0dd802ca053fb72993
Author: Student Coder <student@coder.education>
Date:   Thu Aug 13 11:47:00 2015 -0500

    Sometimes the world needs a "Hello".
```

### Check Out The Differences
It is useful to be able to see what you've changed in a repository in order to select the proper changes for staging and committing.  Create a new file called `new_file`, stage `new_file`, commit the initial file.  Add another line to the file and ask Git for the differences.
```console
$ echo "see me in the diff" > new_file
$ git add new_file
$ git commit -m "added new file for diffing"
$ echo "new line" >> new_file
$ git diff .
```
*results*:
```diff
diff --git a/new_file b/new_file
index bf3322c..a31eb3c 100644
--- a/new_file
+++ b/new_file
@@ -1 +1,2 @@
 see me in the diff
+new line
```

## Conclusions
In this lab you created your own repository, added files, changed files, looked at history, checked status, and committed changes using Git.  Feel free to try all those commands in other different ways and experiment in your new repository.
