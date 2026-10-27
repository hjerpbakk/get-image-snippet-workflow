# get-image-snippet-workflow

Two macOS Automator workflows (Quick Actions) and Python helper scripts that put images into the right folder of the Jekyll site hjerpbakk.com and create the HTML image snippet for a post.

## Run

No build and no tests. The workflows run the scripts on files chosen in Finder.

- Scripts are Python 2 (`print` statements). Resizing needs Pillow, and ImageOptim is used for minifying.
- Paths to the site are hardcoded to `/Users/sankra/projects/sankra.github.io/` in `copy-image.py` and `convert-images-in-posts.py`. They do not follow the current home directory.
- Images are assumed to be 2x, and the snippet is the site's `{% include image.html ... %}` format.
- `convert-images-in-posts.py` is an unfinished stub with a hardcoded post path.
