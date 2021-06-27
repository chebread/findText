# 파일에서 문자열 찾기 (terminal)
import os.path
import sys
def Isfile(file): # 파일이 존재하는가 ?
    if os.path.isfile(file):
        return 1 # 있어요
    else:
        return -1 # 없어요
def Find(file, text):
    isfile = Isfile(file)
    if isfile == -1:
        return -1
    load = open(file, "rb")
    _read_ = load.read()
    load.close()
    decoding = _read_.decode(encoding = "utf-8") # Bytes -> Str
    if decoding.find(text) == -1:
        return -1
    else:
        return 1
def TextInput():
    text = sys.argv[2]
    if text == "q":
        return exit()
    return text
def PathInput():
    file = sys.argv[1]
    if file == "q":
        return exit()
    return file # 경로를 반환해요

path = PathInput()
text = TextInput()
find = Find(path, text)
print(find)
