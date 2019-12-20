import sys
import subprocess
import shutil
import logging
import time

mediaList = ['flash', 'arrow', 'legends', 'blacklist', 
				'bang', 'super', 'kai', 'walking', 
				'supergirl', '100', 'south', 'world','sheldon', 
				'robot', 'walking', 'silicon']

def readFile():
	names = []
	with open('MediaList.txt') as file:
		for line in file:
			line = line.rstrip('\n').lower()
			names.append(line)
	return names

def isWanted(fileName):
	for media in mediaList:
		if media in fileName.lower():
			return True
	return False

def main():

	destPath = 'K:\\Unsorted TV Shows'
	winrarPath = 'C:\\Program Files\\WinRAR\\WinRAR.exe'

	arguments = sys.argv

	torrentName = arguments[1]
	torrentPath = ' '.join(str(elem) for elem in arguments[2:])
	torrentPath = torrentPath.replace('\\', '/')

	if isWanted(torrentName):
		args = [winrarPath, 'x', '-ibck', '-inul', torrentPath + '\\*.r00' , destPath]
		subprocess.call(args)

main()
