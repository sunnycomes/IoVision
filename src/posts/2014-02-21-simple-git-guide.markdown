---
layout: post
title: "Simple Git Guide"
date: 2014-02-21 15:46:05 +0800
comments: true
categories:
tags: Git 
---

##Preliminary

###Remote

If you have not cloned an existing repository and want to connect your repository to a remote server, you need to add it with

	git remote add repo_path

repo_path can be something like `https://github.com/sunnycomes/okcoin_pc`.

###branch

Branches are used to develop features isolated from each other. The master branch is the "default" branch when you create a repository. Use other branches for development and merge them back to the master branch upon completion.

create a new branch named "branch_xx", 

	git branch branch_xx

and switch to it using 
	git checkout branch_xx

or,
	git checkout -b branch_xx

do the same work.

<!-- more -->

###Working Directory, Index, HEAD

your local repository consists of three "trees" maintained by git. the first one is your `Working Directory` which holds the actual files. the second one is the `Index` which acts as a staging area and finally the `HEAD` which points to the last commit you've made.

##Basic Workflow

###checkout a repository

create a working copy of a local repository by running the command

	git clone /path/to/repository 

when using a remote server, your command will be

	git clone username@host:/path/to/repository

###Fetch

Fetch the latest history from the server, use this command
	
	git fetch repo_path

###Add

This is the first step in the basic git workflow. You can propose changes (add it to the Index) using

	git add <filename>

or
	git add *

to add all the untracked files. 

###Commit
To actually commit these changes use

	git commit -m "Commit message, it's necessary for a detail description of the changes."

Now the file is committed to the HEAD, but not in your remote repository yet.

###Merge & Pull
	
To merge another branch into your active branch (e.g. master), use

	git merge master

to update your local repository to the newest commit, execute

	git pull repo_path branch_xx

in your working directory to fetch and merge remote changes, in both cases git tries to auto-merge changes.

Unfortunately, this is not always possible and results in conflicts. You are responsible to merge those conflicts manually by editing the files shown by git. Show unmerged paths which contains conflicts and changes that uncommited,

	git status
	
After changing, you need to mark them as merged with

	git add <filename>

before merging changes, you can also preview them by using

	git diff --cached

Then **commit** all the changes to keep the working  directory **clean**,

	git commit -a -m "Conflicts fixed."


###Push changes

Your changes are now in the HEAD of your local working copy. To send those changes to your remote repository, execute

	git push repo_path branch_xx

Change `branch_xx` to whatever branch you want to push your changes to. 


###Tagging

It's recommended to create tags for software releases. this is a known concept, which also exists in SVN. You can create a new tag named 1.0.0 by executing

	git tag 1.0.0 1b2e1d63ff

the 1b2e1d63ff stands for the first 10 characters of the commit id you want to reference with your tag. You can get the commit id with

	git log

you can also use fewer characters of the commit id, it just has to be unique.

###Reseting

In case you did something wrong (which for sure never happens ;) you can replace local changes using the command

	git checkout -- <filename>

this replaces the changes in your working tree with the last content in HEAD, if it's a new and already tracked file of <filename>, then will be changed to **untracked**. Changes already added to the index, as well as new files, **will be kept**. 

Actually this would not remove the newly added files, this is pretty much like the command line 

	git reset

**however**, such command just make the newly tracked file untracked, the changed content is excluded.
	
	git reset --hard

This command will purge the working directory to the last commits.

If you instead want to drop all your changes or commits

	git reset --hard HEAD_ID

this will remove all the commits after the commit with the *HEAD_ID*.

Fetch the latest history from the server and point your local branch_xx branch at it like this

	git reset --hard repo_path/branch_xx


##References
1. [WIKI Git](http://en.wikipedia.org/wiki/Git_(software))
1. [Git for Small Development Group](http://blog.csdn.net/kasagawa/article/details/6797812)
1. [Getting to Know Git](http://viget.com/extend/getting-to-know-git)
1. [Simple Git Guide, No Deep Shit](http://rogerdudler.github.io/git-guide/)
