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

database=open('notObsolete.txt', 'w')
def file_extension(path): 
  return os.path.splitext(path)[1]

def listFiles(dirPath):
  fileList=[]
  for root,dirs,files in os.walk(dirPath):
    for fileObj in files:
      fileList.append(os.path.join(root,fileObj))
  return fileList

def listDirectDir(dirPath):
  dirList=[]
  for root,dirs,files in os.walk(dirPath):
    for folder in dirs:
      if os.path.isdir(os.path.join(dirPath, folder)) and "textures" not in folder:
        dirList.append(folder)
  return dirList

def GetFileNameAndExt(filename):
  import os
  (filepath,tempfilename) = os.path.split(filename);
  (shotname,extension) = os.path.splitext(tempfilename);
  return shotname

# sys.setdefaultencoding("utf-8");
def main(fileDir):
  folderList = listDirectDir(fileDir)
  for folder in folderList:
    print(folder)
    database.write("%s\n" % folder)
        
main("./common/misc/")
main("./commonwealth/misc/")
main("./europe/misc/")
main("./events/misc/")
main("./france/misc/")
main("./germany/misc/")
main("./italy/misc/")
main("./japan/misc/")
main("./netherlands/misc/")
main("./panamerica/misc/")
main("./panasia/misc/")
main("./russia/misc/")
main("./uk/misc/")
main("./usa/misc/")
database.close()

