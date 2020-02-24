# Contributing

Hi :raised_hands:. We are delighted to see your interest in helping our team build a complete solution for teachers to share notes, assignments with students. Our web app is based on Python's flask framework and its deployed to Heroku: https://notes-ever.herokuapp.com.

Let's get started with setting up the development enviornment for our app to run locally on your system. Please read all the steps below carefully. 

**Note: we recommend executing all the below commands in Bash or any Unix based Terminal. Also, launch your terminal with administrative privileges.** 

## Step #1: Let us Git

First you need to install [Git](https://git-scm.com/). Then you need to fork our repository located at https://github.com/buildHuge/Notes-Ever. 

![a screenshot showing fork button](/docs/forking.png)

After forking you will be redirected to your forked copy. Now let's clone the forked copy.

```bash
git clone https://github.com/<YOUR_GITHUB_USERNAME>/Notes-Ever.git
```

Change directory to the newly downloaded forked copy.

```bash
cd Notes-Ever
```

Now doing `ls` should output the contents `application.py, /notes_ever, sample.env, ...so on`.

In Git usually `origin` is referred to as your forked copy and `upstream` is the original repository from which you forked. And `origin` and `upstream` are called remotes.

So in our case `upstream` is the repo located at https://github.com/buildHuge/Notes-Ever and `origin` is your forked copy at https://github.com/<YOUR_GITHUB_USERNAME>/Notes-Ever.

Git automatically configures the `origin` remote by pointing to the repo from where you cloned. We need to add `upstream` remote by ourselves.

```bash
git remote add upstream https://github.com/buildHuge/Notes-Ever.git
```

Check if remotes were successfully added by typing `git remote -v`. You will get output like this if remotes were added successfully:

```bash
origin  https://github.com/<YOUR_GITHUB_USERNAME>/Notes-Ever.git (fetch)
origin  https://github.com/<YOUR_GITHUB_USERNAME>/Notes-Ever.git (push)
upstream        https://github.com/buildHuge/Notes-Ever.git (fetch)
upstream        https://github.com/buildHuge/Notes-Ever.git (push) 
```

## Step #2: Let's flask run

You need the latest version of [Python](https://www.python.org/) to run the app. After installing Python follow the below process.

```bash
# Reminder: execute the below commands in `Bash` with administrative privileges

# Installs pipenv globally
pip install pipenv

# The below command installs dependencies in a virtualenv using python 3.x.x
pipenv --three install --dev

# Activates virtualenv subshell
pipenv shell

# Copies `sample.env` to `.env` to allow loading of env vars
# You can paste your API credentials in `.env` file
cp sample.env .env

# Runs the app, served at http://localhost:5000 by default
flask run
```

## Step #3: Branching off

We should always work in branches to keep the master undisturbed and enforce a good collaboration enviornment.

Before creating a new branch **ALWAYS** perform the below steps to ensure that when you branch off from `master` you have the latest upstream version.

```bash
# The below command fetches the latest upstream work
git fetch upstream

# Makes sure you are on master
git checkout master

# Reset your local master with upstream/master
git reset --hard upstream/master

# Push to your origin repository
git push --force origin master

# Branching off! Now we can create and switch to a new branch
git checkout -b <A_GOOD_BRANCHNAME>
```

We have switched to a new branch. Now you can make changes to files, add new ones or do whatever you wish.

Once you have made the changes you should `flask run` to test the app. 

## Step #4: Time to send a Pull Request :tada:

If you are satisfied with the changes you can push to `origin` to create a PR.

```bash
# Adds all the modified files
git add .

# Commit the changes
git commit -m "A short descriptive message"

# Push to origin to create a PR
git push origin <NAME_0F_BRANCH_YOU_CREATED>
```
