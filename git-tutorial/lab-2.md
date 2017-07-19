# Lab 2

In this lab you will do the following:
* Learn About Branching and Merging In Git

## Prerequisites
For this lab you will need:
* A Cloud 9 Workspace
* Knowledge of the Basic Commands of Git [See Lab 1](lab-1.md)

## Tasks

### Create and Initialize a Repository
Create a new directory named `lab-2` to work in and initialize a repository there.  Add a file called `README` and commit it to the repository.

> [See Lab 1](lab-1.md) if you need a refresher on the steps

```console
$ mkdir lab-2 && cd lab-2
$ git init .
$ echo "" > README
$ git add README
$ git commit -m "initial repo creation and README addition"
```

### Work with Branches
#### Create a Branch
Make a branch in your new repo called `new_branch`.
```console
$ git branch new_branch
```

Notice that nothing much happened (Git was pretty quiet, right?).  Git created the branch, but didn't move you to that branch.  Your repo is still sitting on the `master` branch.  You can verify this by issuing a `git status` command and looking at the `On branch` output.

#### Change Branches
Let's change to the `new_branch` so we can make some changes.
```console
$ git checkout new_branch
Switched to branch 'new_branch'
```
>Note: if you want to know what branch you are on at any time you can issue the `git status` command and it will tell you.

#### Make Some Changes
Let's make some changes to the files in `new_branch` and see how it affects the repository.  Change the contents of the existing `README` file and create a new file called `useful_info.txt` with some good info in it.
```console
$ echo "This file is redundant" >> README
$ echo "really critical information" > useful_info.txt
```

Stage the changes from both files and commit those to the repository.
```console
$ git add README useful_info.txt
$ git commit -m "committed multiple things in one pass - now with more useful information"
```

At this point your `git status` should return cleanly:
```console
$ git status
On branch new_branch
nothing to commit, working directory clean
```

#### Investigate Differences
Look at the differences between your branch `new_branch` and the `master` branch.
```console
$ git diff master
```
##### Output of the `git diff` Command:
```diff
diff --git a/README b/README
index e69de29..78784bd 100644
--- a/README
+++ b/README
@@ -0,0 +1 @@
+This file is redundant
diff --git a/useful_info.txt b/useful_info.txt
new file mode 100644
index 0000000..524d6b6
--- /dev/null
+++ b/useful_info.txt
@@ -0,0 +1 @@
+really critical information
```

Visualize the history.
```console
$ git log --graph
```

#### Merge Branches
Since our diff looks good it is time for us to merge our `new_branch` branch into `master`.
```console
$ git checkout master
$ git merge new_branch
Updating 271e70d..835d39e
Fast-forward
 README          | 1 +
 useful_info.txt | 1 +
 2 files changed, 2 insertions(+)
 create mode 100644 useful_info.txt
```

If we are all done with our `new_branch` we can delete it.
```console
$ git branch -d new_branch
Deleted branch new_branch (was 835d39e).
```

### Work With Conflicts
We are going to create some artificial conflicts in our repository so you can see how to  work through a conflict scenario.

Create a branch called `nice_feature` and make it the active branch (using the shortcut method).
```console
$ git checkout -b nice_feature
```

Make a change to the README file so that the contents are a the single line.  Stage and commit those changes.
```console
$ echo "These are some changes that will conflict.  Conflict is bad." > README
$ git add README
$ git commit -m "Best change to README evar"
[nice_feature 877d7d1] Best change to README evar
 1 file changed, 1 insertion(+), 1 deletion(-)
```

Switch to the `master` branch and change the README file so the contents are single line.  Stage and commit those changes.
```console
$ git checkout master
Switched to branch 'master'
$ echo "Seemingly mundane change." > README
$ git add README
$ git commit -m "master changes to README"
[master 30d0315] master changes to README
 1 file changed, 1 insertion(+), 1 deletion(-)
```

Our repository now has changes on the `nice_feature` branch that are different from, and in direct conflict with, the changes in the `master` branch.  Let's try to merge the changes from `nice_feature` into `master`.
```console
$ git merge nice_feature
Auto-merging README
CONFLICT (content): Merge conflict in README
Automatic merge failed; fix conflicts and then commit the result.
```

Git gave up on us.  It found the changes were in conflict and said, "It's your problem now buddy".  If you look at the README file you will see the conflicting changes inline with each other.
```diff
<<<<<<< HEAD
Seemingly mundane change.
=======
These are some changes that will conflict.  Conflict is bad.
>>>>>>> nice_feature
```

`HEAD` refers to the latest commit in `master` since it is the branch we are merging into.  The lines between `<<<<<<< HEAD` and `=======` represent the change from `master`.  The lines between `=======` and `>>>>>>> nice_feature` represent the changes from the `nice_feature` branch. You now have to choose the lines you want to keep, so edit the file to represent the text you want (remove all the lines inserted by Git to show you the conflict).  After editing, the file should contain a single line:
```
Seemingly mundane change.
```

Stage the properly merged file and commit the resolved conflict.
```console
$ git add README
$ git commit -m "resolved those nasty conflicts"
[master 24d9480] resolved those nasty conflicts
```


Now take a look at the history to see how it was affected by our conflict fun:
```console
$ git log --graph
*   commit 24d94801173d5455d605279a6757e5895e360638
|\  Merge: 30d0315 877d7d1
| | Author: Student Coder <student@coder.education>
| | Date:   Thu Aug 13 16:55:52 2015 -0500
| |
| |     resolved those nasty conflicts
| |
| * commit 877d7d17faaf4c0269457ba3d2736a0e2ee53597
| | Author: Student Coder <student@coder.education>
| | Date:   Thu Aug 13 16:42:09 2015 -0500
| |
| |     Best change to README evar
| |
* | commit 30d0315b541b54e7ea413dcb7780857127890f91
|/  Author: Student Coder <student@coder.education>
|   Date:   Thu Aug 13 16:45:07 2015 -0500
|
|       master changes to README
|  
* commit 835d39ee0e416c991637b513a7d7c474805ba7e9
| Author: Student Coder <student@coder.education>
| Date:   Thu Aug 13 16:25:54 2015 -0500
|
|     committed multiple things in one pass - now with more useful info
|  
* commit 271e70daa34a7fa91deb4765d42aa8be455d62fc
  Author: Student Coder <student@coder.education>
  Date:   Thu Aug 13 16:24:33 2015 -0500

      added a readme
```

## Conclusion
In this lab you experimented with branching, merging, and resolving conflicts.  Feel free to try all those commands in other different ways and experiment in your new repository.
