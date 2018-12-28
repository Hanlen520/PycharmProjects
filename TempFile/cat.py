from time import ctime,sleep  
import threading;  
import os

class MyThread(threading.Thread):  
    def __init__(self,func,args,name):  
        super(MyThread,self).__init__();  
        self.func=func;  
        self.args=args;  
        self.name=name;  
	self.thread_stop = False              

    def run(self):  
        self.result=self.func(*self.args);  
  
    def getResult(self):  
        return self.result;  
    
    def stop(self):
	self.thread_stop = True

#Get logs when monkey test is running
def logcat():  
    os.popen('adb -s A49947C561B2 logcat -v time > logcat.txt')

#Run monkey test command
def runmonkey():
    os.popen('adb -s A49947C561B2 shell monkey -p com.cootek.test  -p com.android.mms -p com.cootek.smartinputv5 --throttle 10 --ignore-timeouts --ignore-crashes -s 112 -v 1000000 > monkeylog.txt');

#Kill adb process
def killadb():
    os.popen('adb kill-server');

#Install App: Touchpal.apk
def installTouchPal():
    print "Installing TouchPal.apk"
    os.popen('adb -s A49947C561B2 install -r TouchPal.apk');
    print "TouchPal.apk has been installed sucessfully!"

#Uninstall com.cootek.smartinputv5
def uninstallTouchPal():
    os.popen('adb -s A49947C561B2  uninstall com.cootek.smartinputv5');

#Dump memery information where monkey test is running
#	1 per 30 seconds
def dumpMemeryInfo():
    print "dump memeryinfo:"
    os.system('echo "TIME FLAG:"  `date +%d\ %H:%M:%S` >> meminfo.txt');
    os.system('adb -s A49947C561B2 shell dumpsys meminfo com.cootek.smartinputv5 >> meminfo.txt');
    sleep(40);

#Restart adb server by sudo in case sometimes linux can't connect to devices
def restartAdbServer():
 	print "Kill adb server by sudo"
	os.popen('echo -e "CooTek01"|sudo -S /opt/data/cootekime/sdk/platform-tools/adb kill-server')
	print "Adb server has been killed"
	print "Now restarting adb server"
	os.popen('echo -e "CooTek01"|sudo -S /opt/data/cootekime/sdk/platform-tools/adb start-server')	
	print "Adb server started"

def cat():
	os.popen('adb shell input tap 494 1409')

def clearLogcat():
	os.popen("adb -s A49947C561B2 logcat -c")

def tcpdump():
	print "Push 'tcpdump' to '/data/local/tcpdump'"
	os.popen('adb -s A49947C561B2 push /opt/data/cootekime/tcpdump_workspace/tcpdump /data/local/tcpdump')
	print "Change '/data/local/tcpdump's permision"
	os.popen('adb -s A49947C561B2 shell chmod 6755 /data/local/tcpdump')
	os.popen('adb -s A49947C561B2 shell /data/local/tcpdump -i any -p -s 0 -w /sdcard/netCapture.pcap')

#Main Thread
#	1. Restart adb server by sudo in case sometimes linux can't connect to devices
#	2. Install TouchPal.apk
#	3. Start 'adb logcat -v time -> logcat.txt' thread, funciton: logcat()
#	4. Start monkey test thread, function: runmonkey()
#	5. Where monkey test thread is alive, dumpMemeryInfo()
#	6. Kill adb server when monkey test is done
#		then dumpMemeryInfo thread and adb logcat thread are stop too.
def main():  
#	restartAdbServer();
	for i in range(0, 10000):
		print i
		t=MyThread(cat,(),cat.__name__)
		t.start()
		t.stop()

	# t0=MyThread(cat,(),cat.__name__);
	# t0.start();
	# t1=MyThread(cat,(),cat.__name__);
	# t1.start();
	# t2=MyThread(cat,(),cat.__name__);
	# t2.start();
	# t3=MyThread(cat,(),cat.__name__);
	# t3.start();
	# t4=MyThread(cat,(),cat.__name__);
	# t4.start();
	# t5=MyThread(cat,(),cat.__name__);
	# t5.start();
	# t6=MyThread(cat,(),cat.__name__);
	# t6.start();
	# t7=MyThread(cat,(),cat.__name__);
	# t7.start();
	# t8=MyThread(cat,(),cat.__name__);
	# t8.start();
	# t9=MyThread(cat,(),cat.__name__);
	# t9.start();
	# t10=MyThread(cat,(),cat.__name__);
	# t10.start();



#	restartAdbServer();

if __name__=="__main__" :  
	main();

