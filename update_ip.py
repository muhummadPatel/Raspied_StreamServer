from datetime import datetime
from simplegist import Simplegist
from urllib2 import urlopen
import os


f = os.popen('ifconfig wlan0 | grep "inet\ addr" | cut -d: -f2 | cut -d" " -f1')
addr = str(f.read().strip())
#print(addr)

current_time = str(datetime.now())
ip = urlopen('http://ipinfo.io/ip').read().strip()
content = current_time + "   " + addr

gg = Simplegist(username='muhummadPatel', api_token='ed3361fe7630a29900c8ebd47e88ac6d620408e6')
gg.profile().edit(id='b2685c420ce4711601fa9d16f1a05472', content=content)
