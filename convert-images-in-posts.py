#!/usr/bin/env python
# 
# This script takes a folder of Jekyll posts and convert all
# img tags to the following format:
# {% include image.html image="/img/crontab-guru/crontab-guru.png" image-text="crontab guru website" width="869" height="312" %}
#
# By convention, the img folder is a sibling of the given posts folder
# and all images are assumed 2x.

postPath = "/Users/sankra/projects/sankra.github.io/_posts/2018-06-27-do-not-commit-launch-json-in-dotnet-script.md"

print "a"