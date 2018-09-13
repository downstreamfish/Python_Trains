import time
tt = time.time()
lct = time.localtime(tt)
asctm = time.asctime(lct)
print("当前是时间为: ", asctm)
