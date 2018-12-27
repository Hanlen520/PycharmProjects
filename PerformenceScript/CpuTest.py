# coding:utf8
import csv, os, time


# 控制类
class Controller(object):
    def __init__(self, count):
        self.counter = count
        self.alldata = [('timestamp', 'cpustatus')]

    # 单次测试过程
    def testprocess(self):
        result = os.popen("adb shell dumpsys cpuinfo | grep package")
        for line in result.readlines():
            cpuvalue = line.split('%')[0]

        currenttime = self.getCurrentTime()
        self.alldata.append((currenttime, cpuvalue))

    # 多次执行测试过程
    def run(self):
        while self.counter > 0:
            self.testprocess()
            self.counter = self.counter - 1
            time.sleep(5)

    # 获取当前的时间戳
    def getCurrentTime(self):
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return currentTime

    # 数据的存储
    def saveDataCSV(self):
        csvfile = open('cpustatus.csv', 'wb')
        writer = csv.writer(csvfile)
        writer.writerrows(self.alldata)
        csvfile.close()


if __name__=='__main__':
    controller = Controller(10)
    controller.run()
    controller.saveDataCSV()