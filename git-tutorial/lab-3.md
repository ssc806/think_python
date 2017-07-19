# Lab 3

In this lab you will do the following:
* Interact with GitHub

As GitHub is an optional class resource, so this lab also is optional. Even though this is an optional lab, it is recommended so that you can learn about interacting with GitHub.

## Prerequisites
For this lab you will need:
* A Cloud 9 Workspace
* Knowledge of the Basic Commands of Git [See Lab 1](lab-1.md)
* Basic Knowledge of Branching and Merging in Git [See Lab 2](lab-2.md)

## Tasks

### Clone an Existing Repository from GitHub
Clone [the class workspace](https://github.com/ITSE-1402/git-classworkspace) repository from GitHub.
```console
$ git clone git@github.com:ITSE-1402/git-classworkspace.git
Cloning into 'git-classworkspace'...
remote: Counting objects: 3, done.
remote: Compressing objects: 100% (163/163), done.
remote: Total 184 (delta 36), reused 145 (delta 17), pack-reused 0
Receiving objects: 100% (184/184), 3.97 MiB | 3.25 MiB/s, done.
Resolving deltas: 100% (36/36), done.
Checking connectivity... done.
```
> Note: Git created a directory to match the name of the repository you cloned and put the repository in there.

### Branch, Edit, and Push
Create a new branch to make some changes (make up your own branch name).  Make some changes in your branch, stage and commit those changes on your branch.  Push those changes up to GitHub.
```console
$ cd git-classworkspace
$ git checkout -b {my_cool_branchname}
... make some changes ...
$ git add {all_the_changes}
$ git commit -m "description of the changes"
... make sure you add and commit some changes to your branch, otherwise there will be nothing to push to GitHub ...
$ git push origin {my_cool_branchname}
```

Now that your changes are up on GitHub, file a Pull Request based on your new branch.  Go to the [repo](https://github.com/ITSE-1402/git-classworkspace) to file your Pull Request.  While you are there be sure to comment on the Pull Requests from your fellow classmates.

> Note: For more info on Pull Requests go to the [GitHub help page](https://help.github.com/articles/using-pull-requests/)

## Conclusions
In this lab you experimented with collaborating with others in GitHub.  Feel free to try all those commands in other different ways and experiment in your new repository.
