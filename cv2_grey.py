import cv2
import os

path = os.getcwd() + "/sample/anime/"
mk_path = os.getcwd() + "/sample/original"
names = os.listdir(path)
files = [x for x in names if x != ".DS_Store"]

for file in files:
    image = cv2.imread("{0}{1}".format(path, file))
    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    if not os.path.isdir(mk_path): os.makedirs(mk_path)
    if(cv2.imwrite(mk_path + "/" + file, grey)):
        print(file)

print("OK")