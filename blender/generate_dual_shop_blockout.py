"""Generate a provisional graybox for the Grove Street dual-shop concept.

Run in Blender's Scripting workspace or:
  blender --background --python blender/generate_dual_shop_blockout.py

This is a blockout helper, NOT a Sollumz exporter or game-ready MLO. Dimensions
and relative spacing are provisional; survey the actual target area first.
"""
import bpy
import math
import mathutils
import os

CLOTHING = {"x": 0.0, "y": 0.0, "w": 12.0, "d": 10.0, "h": 4.2}
JEWELRY = {"x": 17.0, "y": -1.0, "w": 8.0, "d": 7.0, "h": 3.8}
OUTPUT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "grove_street_dual_shop_blockout.blend")

def mat(name, color, metallic=0.0, roughness=0.65, alpha=1.0):
    m = bpy.data.materials.new(name)
    m.diffuse_color = (*color, alpha)
    m.use_nodes = True
    bsdf = m.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs["Base Color"].default_value = (*color, alpha)
        bsdf.inputs["Metallic"].default_value = metallic
        bsdf.inputs["Roughness"].default_value = roughness
        if "Alpha" in bsdf.inputs:
            bsdf.inputs["Alpha"].default_value = alpha
    if alpha < 1.0:
        try:
            m.surface_render_method = 'DITHERED'
        except Exception:
            pass
    return m

WALL = mat("Blockout_Warm_Concrete", (0.28, 0.30, 0.31))
FLOOR = mat("Blockout_Floor", (0.16, 0.17, 0.18))
GLASS = mat("Blockout_Glass", (0.18, 0.50, 0.56), roughness=0.2, alpha=0.32)
METAL = mat("Blockout_Dark_Metal", (0.07, 0.08, 0.09), metallic=0.6)
WOOD = mat("Blockout_Wood", (0.36, 0.20, 0.11))
WHITE = mat("Blockout_Light", (0.82, 0.81, 0.75))

def cube(name, loc, dims, material=None, bevel=0.0):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc)
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = dims
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    if material:
        obj.data.materials.append(material)
    if bevel:
        mod = obj.modifiers.new("Blockout_Edge", "BEVEL")
        mod.width = bevel
        mod.segments = 2
    return obj

def label(name, body, loc, size, material, rotation=(math.pi/2, 0, 0)):
    curve = bpy.data.curves.new(name + "_Font", type="FONT")
    curve.body = body
    curve.size = size
    curve.extrude = 0.006
    obj = bpy.data.objects.new(name, curve)
    bpy.context.collection.objects.link(obj)
    obj.location = loc
    obj.rotation_euler = rotation
    obj.data.materials.append(material)
    return obj

def shell(spec, brand, subtitle, accent, jewelry=False):
    x, y, w, d, h = (spec[k] for k in ("x", "y", "w", "d", "h"))
    t = 0.22
    cube(brand + "_Floor", (x, y, -0.12), (w, d, 0.24), FLOOR)
    cube(brand + "_RearWall", (x, y+d/2-t/2, h/2), (w, t, h), WALL)
    cube(brand + "_LeftWall", (x-w/2+t/2, y, h/2), (t, d, h), WALL)
    cube(brand + "_RightWall", (x+w/2-t/2, y, h/2), (t, d, h), WALL)
    cube(brand + "_FrontPier_L", (x-w*0.40, y-d/2+t/2, h/2), (w*0.20, t, h), WALL)
    cube(brand + "_FrontPier_R", (x+w*0.40, y-d/2+t/2, h/2), (w*0.20, t, h), WALL)
    sign_y = y-d/2-0.06
    cube(brand + "_SignBoard", (x, sign_y, h-0.40), (w*0.56, 0.14, 0.62), METAL, 0.025)
    label(brand + "_SignText", brand, (x-w*0.245, sign_y-0.08, h-0.48), min(0.42, w/len(brand)*0.65), accent)
    label(brand + "_Subtitle", subtitle, (x-0.75, sign_y-0.085, h-0.76), 0.19, WHITE)
    if jewelry:
        # Partition leaves an opening at the front for staff access.
        cube(brand+"_OfficePartition_L", (x-w*0.16, y+d*0.16, 1.35), (0.16, d*0.36, 2.7), WALL)
        cube(brand+"_OfficePartition_Back", (x+w*0.05, y+d*0.32, 1.35), (w*0.43, 0.16, 2.7), WALL)
        cube(brand+"_SecureOfficeDesk", (x+w*0.13, y+d*0.18, 0.52), (1.35, 0.62, 0.12), WOOD, 0.03)
        for i, dx in enumerate((-1.7, 0.0, 1.7), 1):
            cube(f"{brand}_DisplayCase_{i}", (x+dx, y-0.15, 0.58), (1.12, 0.55, 0.78), METAL, 0.025)
            cube(f"{brand}_DisplayGlass_{i}", (x+dx, y-0.15, 1.02), (1.08, 0.51, 0.08), GLASS)
        cube(brand+"_ServiceCounter", (x-w*0.27, y-d*0.02, 0.55), (1.45, 0.65, 1.1), WOOD, 0.03)
        cube(brand+"_AccentPanel", (x, y-d/2+0.18, 2.4), (w*0.35, 0.12, 0.65), accent)
    else:
        cube(brand+"_Checkout", (x+w*0.28, y-d*0.23, 0.52), (1.55, 0.68, 1.04), WOOD, 0.03)
        for row, yy in enumerate((y-0.3, y+1.2), 1):
            cube(f"{brand}_Rail_{row}_Top", (x-w*0.10, yy, 1.72), (w*0.48, 0.08, 0.08), METAL)
            for i in range(7):
                xx = x-w*0.31+i*(w*0.42/6)
                cube(f"{brand}_Rail_{row}_Support_{i+1}", (xx, yy, 1.35), (0.035, 0.035, 0.72), METAL)
        for i in range(2):
            fx, fy = x-w*0.29+i*1.35, y+d*0.30
            cube(f"{brand}_Fitting_{i+1}_Left", (fx-0.48, fy, 1.25), (0.08, 1.5, 2.5), WOOD)
            cube(f"{brand}_Fitting_{i+1}_Back", (fx, fy+0.72, 1.25), (1.0, 0.08, 2.5), WOOD)
        cube(brand+"_StockShelf_1", (x+w*0.30, y+d*0.28, 1.1), (1.25, 0.42, 2.0), METAL)
        cube(brand+"_StockShelf_2", (x+w*0.30, y+d*0.02, 1.1), (1.25, 0.42, 2.0), METAL)

def aim(obj, target):
    obj.rotation_euler = (mathutils.Vector(target)-obj.location).to_track_quat('-Z', 'Y').to_euler()

def main():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    for datablocks in (bpy.data.meshes, bpy.data.curves, bpy.data.cameras, bpy.data.lights):
        for block in list(datablocks):
            if block.users == 0:
                datablocks.remove(block)
    gold = mat("Brand_Clothing_Amber", (0.88, 0.48, 0.12), metallic=0.15)
    teal = mat("Brand_Jewelry_Teal", (0.10, 0.63, 0.56), metallic=0.15)
    shell(CLOTHING, "GROVE THREADS", "CLOTHING", gold)
    shell(JEWELRY, "GROVE GOLD", "JEWELRY", teal, jewelry=True)
    bpy.ops.object.camera_add(location=(19, -32, 26))
    camera = bpy.context.object
    camera.name = "Review_Camera"
    aim(camera, (10, 0, 0))
    camera.data.lens = 45
    bpy.context.scene.camera = camera
    bpy.ops.object.light_add(type='AREA', location=(10, -12, 20))
    light = bpy.context.object
    light.name = "Review_Area_Light"
    light.data.energy = 3500
    light.data.shape = 'DISK'
    light.data.size = 14
    aim(light, (10, 0, 0))
    bpy.context.scene.render.engine = 'BLENDER_EEVEE_NEXT'
    bpy.context.scene.render.resolution_x = 1400
    bpy.context.scene.render.resolution_y = 900
    bpy.context.scene.render.resolution_percentage = 100
    bpy.ops.wm.save_as_mainfile(filepath=OUTPUT_PATH)
    print("Saved provisional blockout:", OUTPUT_PATH)
    print("Survey exact world placement; finish Sollumz/CodeWalker and in-game validation.")

if __name__ == "__main__":
    main()
