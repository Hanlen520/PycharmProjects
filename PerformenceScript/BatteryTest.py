# coding:utf8
import csv, os, time


# 控制类
class Controller(object):
    def __init__(self, count):
        # 定义测试的参数
        self.counter = count
        # 定义收集数据的数组
        self.alldata = [('timestamp', 'power')]

    # 单次测试过程
    def testprocess(self):
        # 执行获取电量的命令
        result = os.popen('adb shell dumpsys battery')
        # 获取电量的level
        for line in result:
            if "level" in line:
                power = line.split(':')[1]

        # 获取当前的时间
        currenttime = self.getCurrentTime()
        # 将获取到的数据存到数组中
        self.alldata.append((currenttime, power))

    # 多次测试过程
    def run(self):
        # 设置手机进入非充电状态
        os.popen('adb shell dumpsys battery set status 1')
        while self.counter > 0:
            self.testprocess()
            self.counter -= 1
            # 每5秒钟采集一次数据
            time.sleep(5)

    # 获取当前的时间戳
    def getCurrentTime(self):
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return currentTime

    # 数据的存储
    def saveDataToCSV(self):
        csvfile = open('power.csv', 'wb')
        writer = csv.writer(csvfile)
        writer.writerrows(self.alldata)
        csvfile.close()


if __name__ == '__main__':
    controller = Controller(3)
    controller.run()
    controller.saveDataToCSV()