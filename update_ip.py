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

gg = Simplegist(username='muhummadPatel', api_token='[add_github_api_key_here]')
gg.profile().edit(id='[add_github_gist_id_here]', content=content)
