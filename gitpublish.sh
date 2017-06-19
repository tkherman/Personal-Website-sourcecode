#!/bin/bash

# script to automate pushing to github repository
pelican content

cd output
git add *
git commit -m \"$1\"
git push
