import sys
import subprocess
import shutil
import logging

TVShowList = ['flash', 'arrow', 'legends', 'blacklist', 
				'bang', 'super', 'kai', 'walking', 
				'supergirl', '100', 'south', 'world','sheldon', 
				'robot', 'walking', 'silicon']

def printArguments():
	print('Number of arguments:', len(sys.argv))
	print('Argument List:', str(sys.argv))

def isTVShow(fileName):
	if any(show in fileName.lower() for show in TVShowList):
		return True

def main():
	printArguments()

	folderPathName = sys.argv[2] + ' ' + sys.argv[3]
	folderPathName = folderPathName.replace("\\\\", "\\")

	# "C:/Program Files/WinRAR/WinRAR.exe" x -ibck -inul "%F/*.r00" "%F/"

	if isTVShow(sys.argv[1]):
		args = ['C:\\Program Files\\WinRAR\\WinRAR.exe', 'x', '-ibck', '-inul', folderPathName + '\\*.r00' ,'K:\\Unsorted TV Shows']
		subprocess.call(args)
		print('Done!')

main()