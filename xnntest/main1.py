#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import pathlib
import time
from xnntest import a
from xnntest import b


files = ["a.py", "b.py"]
while True:
    for m in range(0, 20000):
        for f in files:
            print(os.system("python3 " + f))
        print("等待一分钟")
        time.sleep(20*60)
# a.set()
# b.get()
# pp="e:\\xiaoniuniu\\apk"
# p=os.listdir(pp)
# for child in p:
#     print(child)
#     if '.apk' in child:
#         print('找到apk')
# ll=os.popen("adb shell rm /sdcard/mm/download/*")
# print(int(19.9))
# timeout=1
# while timeout > 0:
#     print("---------------------------")
#     ll = os.popen("adb shell ls /data/data/com.tencent.android.qqdownloader/files/tassistant/apk")
#     for k in ll:
#         print(k)
#         if '.apk'in k:
#             print('找到apk')
#     timeout=timeout-1

# pp="e:\\xiaoniuniu"
# for child in os.walk(pp):
#     print(child)
    # if clild
# i=os.path.isfile("e:\\xiaoniuniu\\apk\\*.apk")
# i=os.access("e:\\xiaoniuniu\\apk\\base.apk", os.X_OK)
# print(os.path.exists.__doc__)
# p=os.listdir("e:\\xiaoniuniu\\apk\\base.apk")
# print(os.listdir.__doc__)
