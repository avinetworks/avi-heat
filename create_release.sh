#!/bin/bash
set -x
assets=""
git tag -d latest
git tag latest
git push -f origin latest
set -e
for BRANCH in master 16.2 16.1
do
    rm -rf VERSION
    git checkout $BRANCH
    rm -rf dist/
    python setup.py sdist
    mv dist/*tar.gz aviheat-$BRANCH.tar.gz
    assets="$assets -a aviheat-$BRANCH.tar.gz#pip-package-$BRANCH"
done
rm -rf VERSION
git checkout master
/root/bin/hub release edit $assets -F ReleaseNote latest
