from time import ctime, sleep
import os
from threading import *
import sys
import time
import commands

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
    os.system('adb -s %s shell monkey -p com.phonedialer.contact --throttle 10 --ignore-timeouts --ignore-crashes -s 112 -v 10000 >> monkeylog.txt' % (serialNumber))


# Kill adb process
def killadb():
    os.popen('adb -s %s reboot' % (serialNumber))


# Dump memery information where monkey test is running
#	1 per 30 seconds
def dumpMemeryInfo():
    print "dump memeryinfo:"
    os.system('echo "TIME FLAG:"  `date` >> meminfo.txt')
    os.system('adb -s %s shell dumpsys meminfo com.phonedialer.contact  >> meminfo.txt' % (serialNumber))
    sleep(30)


def clearLogcat():
    os.system("adb logcat -c")


def heap():
    print "dump heap"
    num = commands.getoutput('tail -n 200 /var/lib/jenkins/jobs/IME_Dailer_Monkey/workspace/meminfo.txt |grep TOTAL |awk \'{print $2}\'|grep -E \"^[2-9][0-9]{5,10}\"|wc -l')
    if num != '0':
        print num
        now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()); 
        print('adb -s %s shell am dumpheap com.phonedialer.contact /sdcard/heap.hprof' % (serialNumber))
        os.system('adb -s %s shell am dumpheap com.phonedialer.contact /sdcard/heap.hprof' % (serialNumber))
        sleep(10)
        print('dumpheap finish')
        os.system('adb -s %s pull /sdcard/heap.hprof' % (serialNumber))
        print('pull finish')
        #with open('heapInfo.txt', 'a+') as f:
        #    f.write('\n')
        #    f.write(now)
        #    f.write('\n')
        os.system('cat heap.hprof >> heapInfo.txt')
        os.system('rm heap.hprof')


def main():
    print "Enter python"
    t = MyThread(logcat,(),logcat.__name__)
    t.start()
    for i in range(0,99):
        t2 = MyThread(runmonkey, (), runmonkey.__name__)
        t2.start()
    #dump_thread.start();
        print "we are running now!"
        count = 0
        while(t2.isAlive()):
            dumpMemeryInfo()
            count = count + 1
            if count%3 == 0:
                heap()
    if t2.ifdo == False:
        t3 = MyThread(killadb, (), killadb.__name__)
        t3.start()


if __name__ == "__main__":
    serialNumber = sys.argv[1]
    main()
