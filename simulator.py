#! /usr/bin/python

import subprocess
import shlex

if __name__ == '__main__':
	cmd = 'blender empty.blend --background --python initScene.py -- test'
	subprocess.check_call(shlex.split(cmd))
