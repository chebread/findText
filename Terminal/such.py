import sys
import os.path
file = sys.argv[1]
def Isfile(file):
    if os.path.isfile(file) == 1:
        return 1
    else:
        return -1
isfile = Isfile(file)
if isfile == -1:
    print("Error")
else:
    print("%s"%file)