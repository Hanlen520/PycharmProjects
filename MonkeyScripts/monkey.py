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
        return self.result

    def stop(self):
        print 'I am stopping it...'
        self.ifdo = False


# Get logs when monkey test is running
def logcat():
    os.popen('adb logcat -v time > logcat.txt')


# Run monkey test command
def runmonkey():
    os.popen('adb shell monkey -p com.cootek.test -p %s --throttle 10 --ignore-crashes '
             '--ignore-timeouts --ignore-security-exceptions -s 112 -v 10000 >> monkeylog.txt' % packageName)


# Kill adb process
def killadb():
    #os.popen('adb -s N8K7N17606003031 kill-server');
    os.popen('adb reboot')


# Install App: Touchpal.apk
def installTouchPal():
    print "Installing TouchPal.apk"
    os.popen('adb install -r /var/lib/jenkins/workspace/MonkeyTest/TouchPal.apk')
    print "TouchPal.apk has been installed successfully!"


# Uninstall com.cootek.smartinputv5
def uninstallTouchPal():
    os.popen('adb uninstall %s' % packageName)


# Dump memery information where monkey test is running
#	1 per 30 seconds
def dumpMemeryInfo():
    print "dump memeryinfo:"
    os.system('echo "TIME FLAG:"  `date` >> meminfo.txt')
    os.system('adb shell dumpsys meminfo %s >> meminfo.txt' % packageName)
    sleep(30)

# Dump memery information where monkey test is running
    #   1 per 30 seconds
def dumpShopMemeryInfo():
    print "dump memeryinfo:"
    os.system('echo "TIME FLAG:"  `date` >> shop_meminfo.txt');
    os.system('adb -s N8K7N17606003031 shell dumpsys meminfo com.cootek.smartinputv5:mainEntrance >> shop_meminfo.txt');
    sleep(30)

# Restart adb server by sudo in case sometimes linux can't connect to devices
def restartAdbServer():
    print "Kill adb server by sudo"
    #os.popen('adb kill-server')
    os.popen('adb -s N8K7N17606003031 devices')
    print "Adb server has been killed"
    print "Now restarting adb server"
    #os.popen('adb start-server')
    print "Adb server started"


def clearLogcat():
    os.popen("adb logcat -c")


# get memory snapshot
def dump_heap():
    file_name="dump_toucpal_%s" % str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
    # os.popen('adb -s N8K7N17606003031 shell am dumpheap com.cootek.smartinputv5 /sdcard/%s' % file_name)
    os.popen('adb -s N8K7N17606003031 shell am dumpheap com.cootek.smartinputv5  /data/local/tmp/${file_name}.hprof')


# https://www.cnblogs.com/ggjucheng/archive/2012/01/14/2322659.html
def tcpdump():
    print "Push 'tcpdump' to '/data/local/tcpdump'"
    os.popen('adb -s N8K7N17606003031 push /opt/data/cootekime/tcpdump_workspace/tcpdump /data/local/tcpdump')
    print "Change '/data/local/tcpdump's permision"
    os.popen('adb -s N8K7N17606003031 shell chmod 6755 /data/local/tcpdump')
    os.popen('adb -s N8K7N17606003031 shell /data/local/tcpdump -i any -p -s 0 -w /sdcard/netCapture.pcap')


# Main Thread
#	1. Restart adb server by sudo in case sometimes linux can't connect to devices
#	2. Install TouchPal.apk
#	3. Start 'adb logcat -v time -> logcat.txt' thread, funciton: logcat()
#	4. Start monkey test thread, function: runmonkey()
#	5. Where monkey test thread is alive, dumpMemeryInfo()
#	6. Kill adb server when monkey test is done
#		then dumpMemeryInfo thread and adb logcat thread are stop too.
def main():
    # restartAdbServer()
    # clearLogcat()
    uninstallTouchPal()
    installTouchPal()
    t=MyThread(logcat, (), logcat.__name__)
    #dump_thread=MyThread(tcpdump,(),tcpdump.__name__);
    # print "main Thread begins at ",ctime();
    t.start()
    for i in range(0, 99):
        # dump_heap()
        t2 = MyThread(runmonkey, (), runmonkey.__name__)
        t2.start()
    #dump_thread.start();
        print "we are running now!"
        while(t2.isAlive()):
            # dumpShopMemeryInfo()
            dumpMemeryInfo()
    if t2.ifdo == False:
        t3=MyThread(killadb, (), killadb.__name__)
        t3.start()
#	restartAdbServer();

if __name__ == "__main__":
    packageName = sys.argv[1]
    main()
