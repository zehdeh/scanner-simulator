import os
import sys
import bpy
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


scene = bpy.context.scene

scene.unit_settings.system = bpy.utils.units.systems.METRIC
#scene.unit_settings.scale_length = 0.001

for a in bpy.context.screen.areas:
	if a.type == 'VIEW_3D':
		for s in a.spaces:
			if s.type == 'VIEW_3D':
				s.clip_end = 10000

origin=(0,0,0)
bpy.ops.mesh.primitive_ico_sphere_add(location=origin, size=35, subdivisions=4)

calibrationDir = 'Calibrations/20160913110710522/'
for tkaFile in [f for f in os.listdir(calibrationDir) if f.endswith('.tka')]:
	calibProperties = readTKA(calibrationDir + tkaFile)
	R = calibProperties[0]
	T = calibProperties[1:4]
	R2 = np.eye(4)
	R2[:3,:3] = R
	R2[:3,3] = T
	np.set_printoptions(suppress=True)
	print(tkaFile[:-4])
	R3 = np.asarray([np.arctan2(-R[1,2],R[1,1]), np.arctan2(-R[2,0],R[0,0]), np.arcsin(R[1,0])])

	cam = bpy.data.cameras.new("Camera")
	cameraObj = bpy.data.objects.new(tkaFile[:-4], cam)
	scene.objects.link(cameraObj)

	pos = R2.dot([0,0,0,1])
	#R3 = R2.dot([0,0,-1,0])
	print(R3)

	cameraObj.location = (pos[0],pos[2],pos[1])
	cameraObj.rotation_euler = (R3[0],np.pi - R3[1],R3[2])
	cameraObj.scale = (1000,1000,1000)
	cam.clip_end = 10000

	scene.camera = cameraObj

	#bpy.data.scenes['Scene'].render.filepath = '/home/fabian/code/scanner-simulation/image%s.jpg' % cameraName
	#bpy.ops.render.render( write_still=True )
