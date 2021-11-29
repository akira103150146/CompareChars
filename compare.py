import codecs
with codecs.open(r"C:\Users\Akira\FindChar\cn.txt", encoding="utf-8") as cn:
    a = cn.read()
with codecs.open(r"C:\Users\Akira\FindChar\MsgTable.json", encoding="utf-8") as msg:
    b = msg.read()
with codecs.open(r"C:\Users\Akira\FindChar\output.txt", encoding="utf-8", mode="w") as f:
    charsets = {}
    for char in b:
        if char in charsets:
            continue
        else:
            if a.find(char) == -1:
                charsets[char] = True
                f.write(char)
            