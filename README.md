Overview
========

We're making an app for LinkedIn's DevelopHer HackDay: http://hackday.linkedin.com/developher/2012

Dressup Box is like Getaround meets Rent the Runway.

Getting the code
================

To get a local copy of the current code, clone it using git:

    git clone git://github.com/wendykan/dressupbox.git
    cd dressupbox

It's easy to edit this file. Check out this guide to GitHub Flavored Markdown for syntax: http://github.github.com/github-flavored-markdown/

Troubleshooting
===============

If you can't upload a file, check dressupbox/settings.py. In that file, you'll need to change
MEDIA_ROOT and TEMPLATE_DIRS to point to local directories.

If you run

    git push origin master

and you get an error, try running this to resolve the files

    git pull origin master

manually merge the files, type git add to mark them resolved, then recommit and run this

    get push origin master