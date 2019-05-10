# Get Image Snippet Workflows

This repo contains two macOS workflows used to simplify adding images to blogposts on hjerpbakk.com.

1. **Create hjerpbakk.com img folder.** This will create a hjerpbakk.com image folder with the same name as an image, move the image into the new folder, create a transparent placeholder image with the same dimmensions and put the image snippet on the pasteboard, ready to be pasted in the post's Markdown source. The images will also be minified.
2. **Create hjerpbakk.com image snippet.** Given that an image is in its correct folder, this snippet will create a transparent placeholder image with the same dimmensions and put the image snippet on the pasteboard, ready to be pasted in the post's Markdown source. The images will also be minified.

The flow is usually to rename an image to the name of the post, then run script number 1. For subsequent images, first move them to the folder created by script 1, then run script 2 on them. Remember to paste the snippet into the post between each run.

The generated HTML snippet supports both lazy loading and a lightbox.

## Installation

On a clean install of macOS, do the following.

0. Install [ImageOptim](https://imageoptim.com/mac) for maximum minification.
1. Install pip:
    ```shell
    sudo easy_install pip
    ```
2. Install PIL through pip:
    ```shell
    sudo pip install pillow
    ```
3. Open the two workflows and choose `install`.

## Usage

Right click an image and choose any of these two services.