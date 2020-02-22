Check remote: git remote -v

Add remote: git remote add upstream https://github.com/buildHuge/Notes-Ever.git

Before creating branch for PR, update master:
git fetch upstream
git reset --hard upstream/master

Then create branch for PR
git checkout -b BRANCHNAME

git add .
git commit
git push origin BRANCHNAME

Then go to github URL and create PR

To update PR: git push upstream BRANCHNAME
