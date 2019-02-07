### Test CPU speed 
import time
start = time.time()
test = "a test string"
for i in range(100):
    if len(test) < 200000000:
        test += test
    else:
        test = test[0:len(test)//2]
print(time.time() - a)
