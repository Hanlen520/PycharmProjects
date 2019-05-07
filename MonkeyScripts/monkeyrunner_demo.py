#!/usr/bin/python
# -*- coding: utf-8 -*-
#进入网易云音乐，点击查询歌曲

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
#MonkeyRunner.alert('Hello World', 'This is title', 'OK')
#连接设备
device = MonkeyRunner.waitForConnection(3, "CB512FCM14")
#启动应用
device.startActivity("com.netease.cloudmusic/com.netease.cloudmusic.activity.LoadingActivity")
MonkeyRunner.sleep(2)
#点击搜索框
device.touch(1000, 100, "DOWN_AND_UP")
MonkeyRunner.sleep(1)
#输入查询词
device.type('love of my life')
MonkeyRunner.sleep(1)
#点击回车键
device.press('KEYCODE_ENTER', 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
#截图
image = device.takeSnapshot()
image.writeToFile('./neteasemusic.png', 'png')

