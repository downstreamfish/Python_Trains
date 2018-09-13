import time
def procedure():
    time.sleep(2.5)
t0 = time.clock()
procedure()
print(time.clock() - t0)

t1 = time.time()
procedure()
print(time.time() - t1)

