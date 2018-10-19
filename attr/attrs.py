#!/usr/bin/env python
# -*- coding: utf-8 -*-
udids = ["MXF0215911001825", "MXF0215911001825",  # 荣耀7
         ]
newCommandTimeout = 7200
limit_size_4g = 70.0
select_app_limit_size = 70000
mmattr = [{
    'appPackage': 'com.aspire.mm',
    'appActivity': '.app.HotSaleActivity',
    # 'appWaitActivity': 'com.cmcc.cmrcs.android.ui.activities.HomeActivity',
    'unicodeKeyboard': 'True',
    # "resetKeyboard": "True",
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
    # "resetKeyboard": "True",
    "product": "MM",
    "deviceName": "Android",
    'platformName': 'Android',
    "newCommandTimeout": newCommandTimeout,
    "udid": udids[1],  # p10
    "noReset": "True",
}
]

yybattr = [
    {
        'appPackage': 'com.tencent.android.qqdownloader',
        'appActivity': 'com.tencent.pangu.link.SplashActivity',
        'unicodeKeyboard': 'True',
        # "resetKeyboard": "True",
        "product": "yyb",
        "deviceName": "Android",
        'platformName': 'Android',
        "newCommandTimeout": newCommandTimeout,
        "udid": udids[0],  # p7
        "noReset": "True",
    }, {
        'appPackage': 'com.tencent.android.qqdownloader',
        'appActivity': 'com.tencent.pangu.link.SplashActivity',
        'unicodeKeyboard': 'True',
        # "resetKeyboard": "True",
        "product": "yyb",
        "deviceName": "Android",
        'platformName': 'Android',
        "newCommandTimeout": newCommandTimeout,
        "udid": udids[1],  # p7
        "noReset": "True",
    }
]
hwattr = [
    {
        'appPackage': 'com.huawei.appmarket',
        'appActivity': 'com.huawei.appmarket.MainActivity',
        'unicodeKeyboard': 'True',
        # "resetKeyboard": "True",
        "product": "huawei",
        "deviceName": "Android",
        'platformName': 'Android',
        "newCommandTimeout": newCommandTimeout,
        "udid": udids[0],  # p7
        "noReset": "True",
    }, {
        'appPackage': 'com.tencent.android.qqdownloader',
        'appActivity': 'com.tencent.pangu.link.SplashActivity',
        'unicodeKeyboard': 'True',
        # "resetKeyboard": "True",
        "product": "yyb",
        "deviceName": "Android",
        'platformName': 'Android',
        "newCommandTimeout": newCommandTimeout,
        "udid": udids[1],  # p7
        "noReset": "True",
    }
 ]
bdattr = [
    {
        # 'appPackage': 'com.huawei.appmarket',
        # 'appActivity': 'com.huawei.appmarket.MainActivity',
        'appPackage': 'com.baidu.appsearch',
        'appActivity': 'com.baidu.appsearch.SplashActivity',
        # 'appActivity': '.LauncherActivity',
        # 'appWaitActivity': '.distribute.MainActivity',
        # 'appActivity': 'com.baidu.appsearch.distribute.MainActivity',
        #'appWaitActivity': 'com.baidu.appsearch.LauncherActivity',
        'unicodeKeyboard': 'True',
        # "resetKeyboard": "True",
        "product": "baidu",
        "deviceName": "Android",
        'platformName': 'Android',
        "newCommandTimeout": newCommandTimeout,
        "udid": udids[0],  # p7
        "noReset": "True",
    }, {
        'appPackage': 'com.tencent.android.qqdownloader',
        'appActivity': 'com.tencent.pangu.link.SplashActivity',
        'unicodeKeyboard': 'True',
        # "resetKeyboard": "True",
        "product": "qihoo",
        "deviceName": "Android",
        'platformName': 'Android',
        "newCommandTimeout": newCommandTimeout,
        "udid": udids[1],  # p7
        "noReset": "True",
    }
]
qihooattr = [
    {
        'appPackage': 'com.qihoo.appstore',
        'appActivity': '.home.MainActivity',
        # 'appWaitActivity': '.distribute.MainActivity',
        'unicodeKeyboard': 'True',
        # "resetKeyboard": "True",
        "product": "qihoo",
        "deviceName": "Android",
        'platformName': 'Android',
        "newCommandTimeout": newCommandTimeout,
        "udid": udids[0],  # p7
        "noReset": "True",
    }, {
        'appPackage': 'com.tencent.android.qqdownloader',
        'appActivity': 'com.tencent.pangu.link.SplashActivity',
        'unicodeKeyboard': 'True',
        # "resetKeyboard": "True",
        "product": "yyb",
        "deviceName": "Android",
        'platformName': 'Android',
        "newCommandTimeout": newCommandTimeout,
        "udid": udids[1],  # p7
        "noReset": "True",
    }
]