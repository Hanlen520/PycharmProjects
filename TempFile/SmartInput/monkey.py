from time import ctime, sleep
import os
from threading import *
import sys

serialNumber = ''


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


# Get logs when monkey test is running
def logcat():
    os.system('adb -s %s logcat -v time > logcat.txt' % (serialNumber))


# Run monkey test command
def runmonkey():
    os.system('adb -s %s shell monkey -p com.cootek.test  -p com.adroid.mms -p com.cootek.smartinputv5 --throttle 10 --ignore-timeouts --ignore-crashes -s 112 -v 10000 >> monkeylog.txt' % (serialNumber))


# Kill adb process
def killadb():
    os.popen('adb -s %s reboot' % (serialNumber))


# Dump memery information where monkey test is running
#	1 per 30 seconds
def dumpMemeryInfo():
    print "dump memeryinfo:"
    os.system('echo "TIME FLAG:"  `date` >> meminfo.txt')
    os.system('adb -s %s shell dumpsys meminfo com.cootek.smartinputv5 >> meminfo.txt' % (serialNumber))
    sleep(30)


# Dump memery information where monkey test is running
    #   1 per 30 seconds
def dumpShopMemeryInfo():
    print "dump memeryinfo:"
    os.system('echo "TIME FLAG:"  `date` >> shop_meminfo.txt')
    os.system('adb -s %s shell dumpsys meminfo com.cootek.smartinputv5:mainEntrance >> shop_meminfo.txt' % (serialNumber))
    sleep(30);


def clearLogcat():
    os.system("adb logcat -c")


def tcpdump():
    print "Push 'tcpdump' to '/data/local/tcpdump'"
    os.system('adb -s %s push /opt/data/cootekime/tcpdump_workspace/tcpdump /data/local/tcpdump' % (serialNumber))
    print "Change '/data/local/tcpdump's permision"
    os.system('adb -s %s shell chmod 6755 /data/local/tcpdump' % (serialNumber))
    os.system('adb -s %s shell /data/local/tcpdump -i any -p -s 0 -w /sdcard/netCapture.pcap' % (serialNumber))


def main():
    t = MyThread(logcat,(),logcat.__name__);
    t.start()
    for i in range(0,50):
        t2 = MyThread(runmonkey, (), runmonkey.__name__)
        t2.start()
    #dump_thread.start();
        print "we are running now!"
        while(t2.isAlive()):
            dumpShopMemeryInfo();
            dumpMemeryInfo();
    if t2.ifdo == False:
        t3 = MyThread(killadb, (), killadb.__name__);
        t3.start();


if __name__ == "__main__":
    serialNumber = sys.argv[1]
    main()
