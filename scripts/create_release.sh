#!/bin/bash
set -x
assets=""
rm -rf *tar.gz
git checkout master
git tag -d latest
git tag latest
git push -f origin latest
set -e
for BRANCH in master 16.3 17.1
do
    rm -rf VERSION
    git checkout $BRANCH
    git pull --rebase
    rm -rf dist/
    python setup.py sdist
    fname=`ls dist`
    mv dist/$fname ./
    assets="$assets -a $fname#pip-package-$BRANCH"
done
rm -rf VERSION
git checkout master
# hub command compiled from the code at https://github.com/ypraveen/hub
/root/utils/hub release delete latest
/root/utils/hub release create $assets -F ReleaseNote latest
