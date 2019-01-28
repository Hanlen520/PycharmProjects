#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Shengjie.Liu
# @Time    : 2019-01-25 11:41
# @File    : fps_calculate.py
# @Desc    : 计算fps

import sys

"""
adb shell dumpsys gfxinfo <package | pid>
Draw + Prepare + Process + Execute = 完整显示一帧
计算总数据的行数 frame_count = row_num
计算每行渲染时间 render_time = Draw + Prepare + Process + Execute
vsync_overtime_sum 超时帧的总数
当渲染时间>16.67ms(1000/60)，按照垂直同步机制，该帧已经渲染超时
vsync_overtime = 向上取整(render_time/16.67) - 1
比如：
render_time = 66.68 vsync_overtime = 3
render_time = 67 vsync_overtime = 4
# 以60帧为基准
fps = int( frame_count * 60 / (frame_count + vsync_overtime_sum))
"""


def get_fps(raw_data):
    render_time = 0
    jank_count = 0
    vsync_overtime = 0
    with open(raw_data, "r") as f:
        frame_count = len(f.readlines())
        f.seek(0)
        for line in f.readlines():
            time_block = line.split()
            if len(time_block) == 4:
                try:
                    render_time = float(time_block[0]) + float(time_block[1]) + float(time_block[2]) + \
                                  float(time_block[3])
                except ArithmeticError:
                    render_time = 0
            if render_time > 16.67:
                jank_count += 1
                if render_time % 16.67 == 0:
                    vsync_overtime += int(render_time / 16.67) - 1
                else:
                    vsync_overtime += int(render_time / 16.67)
    _fps = int(frame_count * 60 / (frame_count + vsync_overtime))
    print(frame_count, jank_count, vsync_overtime)
    print("-----fps------")
    print(_fps)


if __name__ == "__main__":
    get_fps(sys.argv[1])
