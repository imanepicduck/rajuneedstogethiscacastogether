import shutil
import os
import time

path=input("enter the directory to be sorted")
list=os.listdir(path)
time.time()
for file in list:
  name,ext=os.path.splitext(file)
  ext=ext[1:]
  if ext=="":
      continue 
  if os.path.exists(path+"/"+ext):
      shutil.move(path+"/"+file,path+"/"+ext+"/"+file)
  else:
      os.makedirs(path+"/"+ext)
      shutil.move(path+"/"+file,path+"/"+ext+"/"+file)