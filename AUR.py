import sys
import subprocess
import shutil
import logging
import time

# AutoUnRAR.bat "The.Big.Bang.Theory.S11E05.720p.HDTV.X264-DIMENSION" "X:\\Completed Torrents\\The.Big.Bang.Theory.S11E05.720p.HDTV.X264-DIMENSION"

# python AUR.py "South.Park.S22E10.HDTV.x264-SVA" "K:\Completed Torrents\South.Park.S22E10.HDTV.x264-SVA"


def main():

	destPath = 'K:\\Unsorted TV Shows'
	mediaList = readFile()
	arguments = sys.argv

	print(mediaList)

	torrentName = arguments[1]
	torrentPath = ' '.join(str(elem) for elem in arguments[2:])

	if isWanted(torrentName, mediaList):
		args = ['C:\\Program Files\\WinRAR\\WinRAR.exe', 'x', '-ibck', '-inul', torrentPath + '\\*.r00' , destPath]
		print(args)
		subprocess.call(args)


def printArguments():
	print('Number of arguments:', len(sys.argv))
	print('Argument List:', str(sys.argv))

def readFile():
	names = []
	with open('MediaList.txt') as file:
		for line in file:
			line = line.rstrip('\n').lower()
			names.append(line)

	return names

def writeArguments(args):
	with open('arguments.txt', 'w') as file:
		for arg in args:
			file.write(arg + "\n")

def sanitizeMediaList(mediaList):
	for media in mediaList:
		media = media[:-2].lower()
	return mediaList

def isWanted(fileName, mediaList):
	for media in mediaList:
		if media in fileName.lower():
			return True
	return False
	# if any(name in fileName.lower() for name in mediaList):
	# 	return True

main()
