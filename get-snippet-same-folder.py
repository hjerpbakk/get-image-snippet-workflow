#!/usr/bin/env python
#
# Input is based on the file command with different images as parameters.
# I assume all images are 2x.
# Snippet output looks like this:
# {% include image.html image="/img/crontab-guru/crontab-guru.png" image-text="crontab guru website" width="869" height="312" %}
import sys
from os import path, getcwd
from PIL import Image, ImageDraw
import subprocess

def getNaming(parts):
    pathParts = parts[0].split("/")
    fileName = pathParts[len(pathParts) - 1][:-1]
    folderName = path.basename(path.dirname(parts[0]))
    return folderName, fileName

def getPNGDimensions(parts, divisor):
    i = parts.index("x")
    width = int(parts[i - 1]) / divisor
    height = int(parts[i + 1][:-1]) / divisor
    return width, height

def getJPGDimensions(parts, divisor):
    indices = [i for i, s in enumerate(parts) if 'x' in s]
    i = indices[len(indices) - 1]    
    dimension  = parts[i].split("x")
    width = int(dimension[0]) / divisor
    height = int(dimension[1][:-1]) / divisor
    return width, height

def getGIFDimensions(parts, divisor):
    i = parts.index("x")
    width = int(parts[i - 1]) / divisor
    height = int(parts[i + 1]) / divisor
    return width, height

def getDimensions(image, parts, divisor):
    if "PNG image data" in image:
        dimensions = getPNGDimensions(parts, divisor)
    elif "JPEG image data" in image:
        dimensions = getJPGDimensions(parts, divisor)
    elif "GIF image data" in image:
        dimensions = getGIFDimensions(parts, divisor)
    return dimensions

def createTransparentImage(image, parts):
    dimensions = getDimensions(image, parts, 1) 
    transparentImageName = "/Users/sankra/projects/sankra.github.io/assets/img/" + str(dimensions[0] / 2) + "x" + str(dimensions[1] / 2) + ".png"
    if path.isfile(transparentImageName):
        return

    blank_image = Image.new('RGBA', (dimensions[0], dimensions[1]), (255,255,255,0))
    ImageDraw.Draw(blank_image)
    blank_image.save(transparentImageName)
    subprocess.call(["open", "-a", "ImageOptim", transparentImageName])

def getSnippetOfImage(image):
    parts = image.split()
    createTransparentImage(image, parts)

    naming = getNaming(parts)
    dimensions = getDimensions(image, parts, 2)
    metadata = naming + dimensions
    snippet = "{%% include image.html image=\"/img/%s/%s\" image-text=\"TODO\" width=\"%s\" height=\"%s\" %%}" % (metadata)
    print snippet
 
# https://pillow.readthedocs.io/en/3.0.0/installation.html#os-x-installation
# brew install libtiff libjpeg webp little-cms2
# Install Pillow: sudo /usr/bin/python -m pip install Pillow


# To test:
png = "/Users/sankra/projects/sankra.github.io/img/book-scanner/1iphone5s_silver_landscape.png: PNG image data, 1819 x 785, 8-bit colormap, non-interlaced"
# jpg = "/Users/sankra/Downloads/test/test-images.jpeg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, progressive, precision 8, 600x543, frames 3"
# gif = "/Users/sankra/Downloads/test/test-images.gif: GIF image data, version 89a, 1 x 1"
getSnippetOfImage(png)
# getSnippetOfImage(jpg)
# getSnippetOfImage(gif)