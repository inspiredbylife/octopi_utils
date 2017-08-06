!/usr/bin/env python

# udev rule:
#    echo 'SUBSYSTEM=="tty", ATTRS{idVendor}=="2974", ATTRS{idProduct}=="0503", RUN+="/home/pi/printer_auto_connect.py"' >> /etc/udev/rules.d/98-printer.rules

import urllib3
import json

APIKEY = 'YOUR_API_KEY'

g_header = { 'X-Api-Key': APIKEY, 'Host': "localhost" }
p_header = { 'X-Api-Key': APIKEY, 'Content-Type': 'application/json', 'Host': "localhost" }

data = {
  "command": "connect",
  "port": "/dev/ttyACM0",
}

encoded_data = json.dumps(data).encode('utf-8')

http = urllib3.PoolManager(timeout=urllib3.Timeout(connect=5.0, read=5.0))
r = http.request('GET', 'http://localhost/api/connection', headers=g_header)
if r.status == 200:
    # print r.data
    status = json.loads(r.data.decode('utf-8'))
    state = status.get("current").get("state")
    if state == 'Closed' or state == 'Offline':
        p = http.request('POST', 'http://localhost/api/connection', body = encoded_data, headers = p_header)
        if p.status == 204:
            print "Connected!"
        else:
            print "Unable to connect!"
    else:
        print "State of the printer is %s, printer already connected?" % state
