# 파일에서 문자열을 찾아요
import os.path
def IsFile(file): # 파일이 존재하는가 ?
    if os.path.isfile(file):
        return 1 # 있어요
    else:
        return -1 # 없어요
def Find(file, text):
    load = open(file, "rb")
    _read_ = load.read()
    decoding = _read_.decode(encoding = "utf-8") # Bytes -> Str
    if decoding.find(text) == -1:
        return -1
    else:
        return 1
def Result(result, text, file):
    if result == 1:
        return "-> %s 경로에 %s 라는 문자열이 존재해요 <-"%(file, text)
    else:
        return "-> %s 경로에 %s 라는 문자열은 존재하지 않아요 <-"%(file, text)
def TextInput():
    text = str(input("문자열(q:quit): "))
    if text == "q":
        print("종료")
        exit()
    return text
def PathInput():
    file = str(input("경로(q:quit): "))
    if file == "q":
        print("종료")
        exit()
    return file # 경로를 반환해요
print("문자열 찾기")
while True:
    file = PathInput()
    text = TextInput()
    find = Find(file, text)
    print(Result(find, text, file))