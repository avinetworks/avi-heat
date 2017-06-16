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
/root/bin/hub release edit $assets -F ReleaseNote latest
