from time import ctime, sleep
import os
import datetime
from threading import *
import sys

packageName = ""

class MyThread(Thread):
    def __init__(self, func, args, name):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args
        self.name = name
        self.ifdo = False
    def run (self):
        self.ifdo = True
        self.result = self.func(*self.args)
        self.ifdo = False

    def getResult(self):
        return self.result;

    def stop (self):
        print 'I am stopping it...'
        self.ifdo = False;


def clearLogcat():
    os.popen("adb logcat -c")


# Get logs when monkey test is running
def logcat():
    os.popen('adb logcat -v time > log.txt')


# Run monkey test command
def runmonkey():
    os.popen('adb shell monkey -p %s --pct-touch 40 --pct-motion 25 --pct-appswitch 10 --pct-rotation 5 '
             '--ignore-crashes --ignore-timeouts --ignore-security-exceptions -s 1024 --throttle 200 -v 100 '
             '1>monkey_log.txt 2>error.txt' % packageName)


# Kill adb process
def killadb():
    os.popen('adb kill-server')


# Dump memery information where monkey test is running
#	1 per 30 seconds
def dumpMemeryInfo():
    # print "dump memeryinfo:"
    os.system('echo "TIME FLAG:"  `date "+%Y-%m-%d %H:%M:%S"` >> meminfo.txt')
    os.system('adb shell dumpsys meminfo %s >> meminfo.txt' % packageName)
    sleep(30)


# Main Thread
#	1. Restart adb server by sudo in case sometimes linux can't connect to devices
#	2. Install TouchPal.apk
#	3. Start 'adb logcat -v time -> logcat.txt' thread, funciton: logcat()
#	4. Start monkey test thread, function: runmonkey()
#	5. Where monkey test thread is alive, dumpMemeryInfo()
#	6. Kill adb server when monkey test is done
#		then dumpMemeryInfo thread and adb logcat thread are stop too.
def main():
    clearLogcat()
    t = MyThread(logcat, (), logcat.__name__)
    t.start()
    for i in range(0, 5):
        t2 = MyThread(runmonkey, (), runmonkey.__name__)
        t2.start()
        # print "we are running now!"
        while(t2.isAlive()):
            dumpMemeryInfo()
    if t2.ifdo == False:
        t3 = MyThread(killadb, (), killadb.__name__);
        t3.start()


if __name__ == "__main__":
    packageName = sys.argv[1]
    main()
