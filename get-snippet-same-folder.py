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

def createSrcsetItem(folder, filename, width):
    return "/img/" + folder + "/" + filename + " " + width + "w, "

def createSmallerImages(image, parts, naming):
    imagePath, fileExtension = path.splitext(parts[0])
    fileExtension = fileExtension[:-1]
    fileName = naming[1].split(".")[0]
    folderName = naming[0]
    originalImage = Image.open(imagePath + fileExtension)
    dimensions = getDimensions(image, parts, 1)
    supportedWidths = [ 2304, 2049, 1563, 1366, 1024, 750, 640 ]
    srcset = ""
    originalSizeUnused = True
    for i in range(0, 7):
        filePostfix = ""
        if (dimensions[0] > supportedWidths[i]):
            
            resizeRatio = supportedWidths[i] / float(dimensions[0])
            newHeight = int(round(dimensions[1] * resizeRatio))
            newImage = originalImage.resize((supportedWidths[i], newHeight), Image.ANTIALIAS)
            filePostfix = "_" + str(supportedWidths[i]) + fileExtension
            newImage.save(imagePath + filePostfix, quality=100)
            srcset += createSrcsetItem(folderName, fileName + filePostfix, str(supportedWidths[i]))
        elif (originalSizeUnused):
            # Use original width once if image is too small to utilise entire scale
            originalSizeUnused = False
            filePostfix = "_" + str(dimensions[0]) + fileExtension
            originalImage.save(imagePath + filePostfix)
            srcset += createSrcsetItem(folderName, fileName + filePostfix, str(dimensions[0]))
        subprocess.call(["open", "-a", "ImageOptim", imagePath + filePostfix])
    return srcset[:-2]
        
def getSnippetOfImage(image):
    parts = image.split()
    naming = getNaming(parts)
    srcset = createSmallerImages(image, parts, naming)
    dimensions = getDimensions(image, parts, 2)
    metadata = naming + dimensions + (srcset,)
    # TODO: Need multiples of this script, 1x, 2x (this) and 3x
    snippet = "{%% include image.html image=\"/img/%s/%s\" image-text=\"TODO\" width=\"%s\" height=\"%s\" srcset=\"%s\" %%}" % (metadata)
    print snippet
 
# https://pillow.readthedocs.io/en/3.0.0/installation.html#os-x-installation
# brew install libtiff libjpeg webp little-cms2
# Install Pillow: sudo /usr/bin/python -m pip install Pillow


# To test:
png = "/Users/sankra/projects/sankra.github.io/img/signing-commits-github-desktop/signing-commits-github-desktop.png: PNG image data, 2120 x 1428, 8-bit colormap, non-interlaced"
# jpg = "/Users/sankra/Downloads/test/test-images.jpeg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, progressive, precision 8, 600x543, frames 3"
# gif = "/Users/sankra/Downloads/test/test-images.gif: GIF image data, version 89a, 1 x 1"
getSnippetOfImage(png)
# getSnippetOfImage(jpg)
# getSnippetOfImage(gif)