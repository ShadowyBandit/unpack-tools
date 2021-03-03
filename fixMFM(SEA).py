import os
import hashlib;
import sys;
import re
import time
import importlib
importlib.reload(sys);
import warnings
import xml.etree.ElementTree as ET
warnings.filterwarnings("ignore")
def file_extension(path): 
  return os.path.splitext(path)[1]

def listFiles(dirPath):

    fileList=[]

    for root,dirs,files in os.walk(dirPath):

        for fileObj in files:

            fileList.append(os.path.join(root,fileObj))

    return fileList

def GetFileNameAndExt(filename):
    import os
    (filepath,tempfilename) = os.path.split(filename);
    (shotname,extension) = os.path.splitext(tempfilename);
    return shotname

# sys.setdefaultencoding("utf-8");
def main(fileDir):

    regex = r'FUNC_SYS_ADD_ACCDETAIL'

    fileList = listFiles(fileDir)

    for fileObj in fileList:
        if file_extension(fileObj) == '.mfm':
            print(fileObj)
            tree = ET.parse(fileObj)
            #tree.write("%s2" % fileObj)
            root = tree.getroot()
            for child in root:
                if len(child)>0 and "ship_atlas_detail" in child[0].text:
                    child[0].text="content/gameplay/common/textures/ship_atlas_detail.dds"
                if len(child)>0 and "transparent_glass_alpha_a" in child[0].text:
                    child[0].text="content/gameplay/common/textures/transparent_glass_alpha_a.dds"
                if "fx" in child.tag:
                    if 'shaders/std_effects/PBS.fx' in child.text:
                        child.text='shaders/materials/pbs/ship_nodamage_material.fx'
                    elif 'shaders/std_effects/PBS_ship.fx' in child.text:
                        child.text='shaders/materials/pbs/ship_material.fx'
                    elif 'shaders/std_effects/PBS_ship_skinned.fx' in child.text:
                        child.text='shaders/materials/pbs/ship_material_skinned.fx'
                    elif 'shaders/std_effects/PBS_emissive.fx' in child.text:
                        child.text='shaders/materials/pbs/ship_emissive_material.fx'
                    elif 'shaders/std_effects/PBS_ship_emissive.fx' in child.text:
                        child.text='shaders/materials/pbs/ship_emissive_material.fx'
                    elif 'shaders/std_effects/PBS_skinned_emissive.fx' in child.text:
                        child.text='shaders/materials/pbs/ship_emissive_material_skinned.fx'
                    elif 'shaders/std_effects/PBS_wire.fx' in child.text:
                        child.text='shaders/materials/pbs/wire_material.fx'
                    elif 'shaders/std_effects/ship_material.fx' in child.text:
                        child.text='shaders/materials/pbs/ship_material.fx'
                    elif 'shaders/std_effects/ship_material_skinned.fx' in child.text:
                        child.text='shaders/materials/pbs/ship_material_skinned.fx'
                    elif 'shaders/std_effects/wire_material.fx' in child.text:
                        child.text='shaders/materials/pbs/wire_material.fx'
                    elif 'shaders/std_effects/ship_nodamage_material.fx' in child.text:
                        child.text='shaders/materials/pbs/ship_nodamage_material.fx'
            tree.write(fileObj)

if os.path.exists("./aircraft/"):
    main("./aircraft/")
if os.path.exists("./catapult/"):
    main("./catapult/")
if os.path.exists("./director/"):
    main("./director/")
if os.path.exists("./finder/"):
    main("./finder/")
if os.path.exists("./gun/"):
    main("./gun/")
if os.path.exists("./projectile/"):
    main("./projectile/")
if os.path.exists("./radar/"):
    main("./radar/")
if os.path.exists("./ship/"):
    main("./ship/")
