# James Vella Blender Scripts
My collection of Blender scripts. Currently written for Blender 3.0

<br />

# Script descriptions

<br />

### jv_convert_to_glb.py

#### How to use
- Download the jv_convert_to_glb.py and Waterbottle.glb files
- Copy the Waterbottle.glb to a perminent location as the script will always reference this directory
- Copy the jv_convert_to_glb.py to your blender startup directory: blender-3.0.0-stable\3.0\scripts\startup
- Open the jv_convert_to_glb.py and change your directory in this line: bpy.ops.import_scene.gltf(filepath="C:\\\Your\\\Path\\\To\\\The\\\Waterbottle.glb"
- Start blender
- To access the tool open Blender > press N > Tool > Convert to GLB

##### Notes:
- This script works in conjunction with the exporter from 3dsmax: [JV_VrayToBlenderGLB.ms](https://github.com/jmdvella/3dsmax-scripts/blob/main/JV_VrayToBlenderGLB.ms)
- First open your 3dsmax scene with your prepared Vray Roughness materials.
- Convert your scene using the JV_VrayToBlenderGLB.ms
- Export to FBX
- Import the FBX to blender
- Run the Convert to 'GLB script' in blender (follow instructions above)
   

