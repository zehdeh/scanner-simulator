#! /usr/bin/python

import sys
import subprocess
import shlex
import numpy as np

def readTKA(fileName):
	tkaFile = open(fileName, 'r')
	lines = tkaFile.readlines()

	rotationLines = lines[1:4]
	rotationMatrix = list()
	for line in rotationLines:
		line = line.split()
		line = [float(i) for i in line]
		rotationMatrix.append(line)
	rotationMatrix = np.asarray(rotationMatrix)
	X,Y,Z = [float(line.split()[1]) for line in lines[4:7]]
	f,K1,K2,S,x,y,a,b = [float(line.split()[1]) for line in lines[7:15]]
	rs = [float(i) for i in lines[15].split()[1:3]]
	c = float(lines[16].split()[1])
	return rotationMatrix,X,Y,Z,f,K1,K2,S,x,y,a,b,rs,c

if __name__ == '__main__':
	cmd = 'blender empty.blend --background --python initScene.py -- test'
	subprocess.check_call(shlex.split(cmd))
