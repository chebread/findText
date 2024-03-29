# 파일에서 문자열 찾기 (simple)
import os.path
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
    decoding = _read_.decode(encoding = "utf-8") # Bytes -> Str
    if decoding.find(text) == -1:
        return -1
    else:
        return 1
def Exit():
    print("Exit")
    print("POWER BY PYTHON")
    return exit()
def TextInput():
    text = str(input("Text: "))
    if text == "q":
        Exit()
    return text
def PathInput():
    file = str(input("Path: "))
    if file == "q":
        Exit()
    return file # 경로를 반환해요
print("Find Text")
while True:
    file = PathInput()
    text = TextInput()
    find = Find(file, text)
    print(find)