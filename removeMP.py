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

goodDatabase = []

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
  fileList = listFiles(fileDir)
  for fileObj in fileList:
    if file_extension(fileObj) == '.visual':
      print(fileObj)
      tree = ET.parse(fileObj)
      tree.write("%s2" % fileObj)
      root = tree.getroot()
      removeMP(root)
      tree.write(fileObj)
      

def removeMP(node):
  bad = []
  good = []
  for child in node:
    if len(child)>0 and "node" in child.tag and ("MP_" in child[0].text or "SP_" in child[0].text) and (child[0].text.split("_")[1] not in goodDatabase):
      print(child[0].text)
      bad.append(child)
    else:
      good.append(child)
  for badChild in bad:
    node.remove(badChild)
  for goodChild in good:
    removeMP(goodChild)
        
def setDatabase():
  with open('notObsolete.txt', 'r') as database:
    filecontents = database.readlines()
    for line in filecontents:
        current_place = line[:-1]
        goodDatabase.append(current_place)

setDatabase()
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

