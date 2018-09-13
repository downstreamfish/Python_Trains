try:
    with open('nofile.txt','r') as f:
        for line in f:
            print(f)
except OSError as err:
    print("出错了:", err)
