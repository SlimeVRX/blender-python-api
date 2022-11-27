# bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False,
#                                 location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False,
#                                                             False, False, False, False, False, False, False, False, False, False, False, False))

bpy.ops.mesh.primitive_cube_add(size=2.0, 
                                calc_uvs=True, 
                                enter_editmode=False, 
                                align='WORLD', 
                                location=(0.0, 0.0, 0.0), 
                                rotation=(0.0, 0.0, 0.0), 
                                scale=(1.0, 1.0, 1.0)
                               )
