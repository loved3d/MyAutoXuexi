#!/usr/bin/env python
# -*- coding:utf-8 -*-
import uiautomator2 as u2
d = u2.connect('10.176.140.132')
print(d.info)
d.app_start("com.kugou.android", ".app.splash.SplashActivity")
d(text="登录").click()
d(text="帐号登录").wait(timeout=10.0)
d.app_stop("com.kugou.android")