import sys
import bpy

origin=(0,0,0)
bpy.ops.mesh.primitive_uv_sphere_add(location=origin)

bpy.data.scenes['Scene'].render.filepath = '/home/fabian/code/scanner-simulation/image.jpg'
bpy.ops.render.render( write_still=True )
