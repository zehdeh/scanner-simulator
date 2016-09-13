import sys
import bpy
import numpy as np

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

for cameraName, offset in zip(['05_A','05_B'],[100.0,-100.0]):
	cam = bpy.data.cameras.new("Camera")
	cameraObj = bpy.data.objects.new(cameraName, cam)
	scene.objects.link(cameraObj)

	cameraObj.location = (offset,-1000.0,0.0)
	cameraObj.rotation_euler = (np.pi/2,0.0,0.0)
	cameraObj.scale = (1000,1000,1000)
	cam.clip_end = 10000

	scene.camera = cameraObj

	bpy.data.scenes['Scene'].render.filepath = '/home/fabian/code/scanner-simulation/image%s.jpg' % cameraName
	bpy.ops.render.render( write_still=True )
