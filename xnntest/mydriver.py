
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time

from appium import webdriver
udids = ["X2P5T15921000817", "W8RDU15917003121"]
newCommandTimeout = 3600
mmattr = [{
    'appPackage': 'com.aspire.mm',
    'appActivity': '.app.HotSaleActivity',
    # 'appWaitActivity': 'com.cmcc.cmrcs.android.ui.activities.HomeActivity',
    'unicodeKeyboard': 'True',
    'automationName': 'uiautomator2',
    'noReset': 'False',
    "product": "MM",
    "deviceName": "Android",
    'platformName': 'Android',
    "newCommandTimeout": newCommandTimeout,
    "udid": udids[0],  # 荣耀7
    "noReset": "True",
}, {
    'appPackage': 'com.aspire.mm',
    'appActivity': '.app.HotSaleActivity',
    # 'appWaitActivity': 'com.cmcc.cmrcs.android.ui.activities.HomeActivity',
    'unicodeKeyboard': 'True',
    'automationName': 'uiautomator2',
    "product": "MM",
    "deviceName": "Android",
    'platformName': 'Android',
    "newCommandTimeout": newCommandTimeout,
    "udid": udids[1],  # p10
    "noReset": "True",
}
]
desired_capabilities = mmattr[0]



def get_driver():
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_capabilities)
    return driver


