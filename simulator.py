#! /usr/bin/python

import sys
import subprocess
import shlex
import numpy as np
import cv2


if __name__ == '__main__':
	#calibProperties = readTKA(sys.argv[1])
	#R = calibProperties[0]
	#T = calibProperties[1:4]
	#T = -R.dot(T)
	#r,J = cv2.Rodrigues(np.require(R, dtype=np.float64))
	#print np.asarray([np.arctan2(-R[1,2],R[1,1]), np.arctan2(-R[2,0],R[0,0]), np.arcsin(R[1,0])])*180/np.pi

	"""
	R2 = np.eye(4)
	R2[:3,:3] = R
	R2[:3,3] = T
	np.set_printoptions(suppress=True)
	print R2
	print R2.dot([0,0,0,1])

	sys.exit(0)
	"""
	#cmd = 'blender empty.blend --background --python initScene.py -- test'
	cmd = 'blender empty.blend --python initScene.py -- test'
	subprocess.check_call(shlex.split(cmd))
