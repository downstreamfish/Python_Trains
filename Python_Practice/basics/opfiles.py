#基本的文件操作,包括open,read,write
with open('test.txt', 'wt') as out_file:
    out_file.write("该文本会写入到文件中\n卡到我了吧!")

with open('test.txt', 'rt') as in_file:
    text = in_file.read()

print(text)
