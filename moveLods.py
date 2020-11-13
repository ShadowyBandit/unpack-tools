import os
import hashlib;
import sys;
import re
import time
import importlib
import shutil
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

def listDirectFiles(dirPath):
  fileList=[]
  for root,dirs,files in os.walk(dirPath):
    for fileObj in files:
      if os.path.exists(os.path.join(dirPath,fileObj)):
        fileList.append(os.path.join(root,fileObj))
  return fileList

def GetFileNameAndExt(filename):
  import os
  (filepath,tempfilename) = os.path.split(filename);
  (shotname,extension) = os.path.splitext(tempfilename);
  return shotname

# sys.setdefaultencoding("utf-8");
def main(fileDir):
  fileList = listDirectFiles(fileDir)
  if not os.path.exists(os.path.join(fileDir, "lods")):
    os.mkdir(os.path.join(fileDir, "lods")) 
  for fileObj in fileList:
    if file_extension(fileObj) == '.model':
      tree = ET.parse(fileObj)
      tree.write("%s2" % fileObj)
      print(fileObj)
      root = tree.getroot()
      for child in root:
        if child.text and "_lod" in child.text and "lods" not in child.text:
          print(child.text)
          child.text=os.path.join("%s/lods/" %os.path.split(child.text)[0],os.path.split(child.text)[1])
      tree.write(fileObj)
    if "lod" in fileObj:
      shutil.move(fileObj, os.path.join(fileDir, "lods"))
      if file_extension(fileObj) == '.model':
        shutil.move("%s2" % fileObj, os.path.join(fileDir, "lods"))
      
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
if os.path.exists("./misc/"):
    main("./misc/")
if os.path.exists("./radar/"):
    main("./radar/")
if os.path.exists("./projectile/"):
    main("./projectile/")
if os.path.exists("./ship/"):
    main("./ship/")

