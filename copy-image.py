#!/usr/bin/env python
#
# Moves an image to an appropriate folder in the img folder of a Jekyll webiste.
import os

def getNaming(imagePath):
    parts = imagePath.split("/")
    fileName = parts[len(parts) - 1]
    fileNameParts = fileName.split(".")
    folderName = fileNameParts[len(fileNameParts) - 2]
    return folderName, fileName

def moveImageToImgFolder(oldPath, naming):
    rootFolder = "/Users/sankra/projects/sankra.github.io/img/"
    imageFolder = rootFolder + naming[0] + "/"
    try:
        os.makedirs(imageFolder)
    except OSError:
        if not os.path.isdir(imageFolder):
            raise
    newName = imageFolder + naming[1]
    os.rename(oldPath, newName)
    return newName

def findPathAndMoveImageToImgFolder(imagePath):
    naming = getNaming(imagePath)
    oldPath = imagePath
    newName = moveImageToImgFolder(oldPath, naming)
    print newName