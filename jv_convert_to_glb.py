bl_info = {
    "name": "JV Convert to GLB",
    "blender": (3, 0, 0),
    "category": "Object",
    "location": "3D Viewport",
}

import bpy

class SimpleOperator(bpy.types.Operator):
    bl_idname = "object.convert_to_glb"
    bl_label = "Convert to GLB"
   
    def execute(self, context):
    
    
        # Define the name of the original node group (update this with the correct name)
        original_node_group_name = "glTF Settings"

        # Check if the WaterBottle object exists
        waterbottle = bpy.context.scene.objects.get("WaterBottle")

        if not waterbottle:
            bpy.ops.import_scene.gltf(filepath="C:\\Your\\Path\\To\\The\\Waterbottle.glb", files=[{"name":"Waterbottle.glb", "name":"Waterbottle.glb"}], loglevel=50)
            waterbottle = bpy.context.scene.objects.get("WaterBottle")

        if waterbottle:
            # Get the original node group
            original_node_group = bpy.data.node_groups.get(original_node_group_name)

            if original_node_group:
                print(f"Original node group '{original_node_group_name}' found.")

                # Iterate through all objects in the scene
                for obj in bpy.context.scene.objects:
                    # Skip the waterbottle itself
                    if obj == waterbottle:
                        continue

                    if obj.material_slots:
                        for material_slot in obj.material_slots:
                            existing_mat = material_slot.material

                            # Create a copy of the glTF Settings group
                            new_node_group = existing_mat.node_tree.nodes.new('ShaderNodeGroup')
                            new_node_group.node_tree = original_node_group
                            new_node_group.location = (0, -400)

                            if existing_mat.use_nodes:
                                principled_bsdf = existing_mat.node_tree.nodes.get("Principled BSDF")
                                if principled_bsdf and principled_bsdf.inputs["Specular"].is_linked:
                                    connected_node = principled_bsdf.inputs["Specular"].links[0].from_node
                                    existing_mat.node_tree.links.new(connected_node.outputs["Color"], new_node_group.inputs["Occlusion"])
                                    existing_mat.node_tree.links.remove(principled_bsdf.inputs["Specular"].links[0])

        # Delete the imported water bottle
        if waterbottle:
            bpy.data.objects.remove(waterbottle, do_unlink=True)

        # Iterate through all objects in the scene
        for obj in bpy.context.scene.objects:
            if obj.material_slots:
                for material_slot in obj.material_slots:
                    existing_mat = material_slot.material
                    if existing_mat.use_nodes:
                        uvw_map_node = existing_mat.node_tree.nodes.new(type="ShaderNodeUVMap")
                        uvw_map_node.location = (-800, -100)
                        uvw_map_node.uv_map = "UVMap"  # Change to the name of your UV map


        return {'FINISHED'}

class SimplePanel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_vella_panel"
    bl_label = "Vella"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Tool"
   
    def draw(self, context):
        layout = self.layout
        layout.operator("object.convert_to_glb")

bpy.utils.register_class(SimpleOperator)
bpy.utils.register_class(SimplePanel)

def menu_func(self, context):
    self.layout.operator("object.convert_to_glb")

def register():
    bpy.utils.register_class(SimpleOperator)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(SimpleOperator)
    bpy.types.VIEW3D_MT_object.remove(menu_func)

if __name__ == "__main__":
    register()