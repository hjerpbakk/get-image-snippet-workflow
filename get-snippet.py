#!/usr/bin/env python
#
# Input is based on the file command with different images as parameters.
# I assume all images are 2x.
# Snippet output looks like this:
# {% include image.html image="/img/crontab-guru/crontab-guru.png" image-text="crontab guru website" width="869" height="312" %}
#
# To test:
# png = "/Users/sankra/Downloads/test/test-images.png: PNG image data, 709 x 492, 8-bit colormap, non-interlaced"
# jpg = "/Users/sankra/Downloads/test/test-images.jpeg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, progressive, precision 8, 600x543, frames 3"
# gif = "/Users/sankra/Downloads/test/test-images.gif: GIF image data, version 89a, 1 x 1"
# getSnippetOfImage(png)
# getSnippetOfImage(jpg)
# getSnippetOfImage(gif)

def getNaming(parts):
    pathParts = parts[0].split("/")
    fileName = pathParts[len(pathParts) - 1][:-1]
    fileNameParts = fileName.split(".")
    folderName = fileNameParts[len(fileNameParts) - 2]
    return folderName, fileName

def getPNGDimensions(parts):
    i = parts.index("x")
    width = int(parts[i - 1]) / 2
    height = int(parts[i + 1][:-1]) / 2
    return width, height

def getJPGDimensions(parts):
    indices = [i for i, s in enumerate(parts) if 'x' in s]
    i = indices[len(indices) - 1]    
    dimension  = parts[i].split("x")
    width = int(dimension[0]) / 2
    height = int(dimension[1][:-1]) / 2
    return width, height

def getGIFDimensions(parts):
    i = parts.index("x")
    width = int(parts[i - 1]) / 2
    height = int(parts[i + 1]) / 2
    return width, height

def getSnippetOfImage(image):
    parts = image.split()
    naming = getNaming(parts)
    if "PNG image data" in image:
        dimensions = getPNGDimensions(parts)
    elif "JPEG image data" in image:
        dimensions = getJPGDimensions(parts)
    elif "GIF image data" in image:
        dimensions = getGIFDimensions(parts)

    metadata = naming + dimensions
    snippet = "{%% include image.html image=\"/img/%s/%s\" image-text=\"TODO\" width=\"%s\" height=\"%s\" %%}" % (metadata)
    print snippet
