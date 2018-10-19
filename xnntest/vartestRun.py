import os
import time

files = ["vartest2.py","vartest1.py"]
for m in range(0, 20):
    for f in files:
        print("-----------------------------")
        os.system("python3 "+f)
    print("等待一分钟")
    time.sleep(60)