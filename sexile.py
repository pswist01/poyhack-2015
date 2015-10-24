from flask import Flask, render_template, request
from zeroconf import ServiceBrowser, Zeroconf
from six.moves import input

import json
import requests

app = Flask(__name__, template_folder=".")

@app.route('/')
def mainview():
        return render_template('index.html')
    
@app.route('/tripadvisor/')
def trip():
        url = "http://api.tripadvisor.com/api/partner/2.0/location/89575?key=5A21D499D9BD4ECBAEDD8DDA312AB087"
        values = json.loads(requests.get(url).content)
        for item in values:
                print item
                print values[item]
        return "poop"



"""class MyListener(object):

    def remove_service(self, zeroconf, type, name):
        print("Service %s removed" % (name,))

    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        print("Service %s added, service info: %s" % (name, info))

zeroconf = Zeroconf()
listener = MyListener()
browser = ServiceBrowser(zeroconf, "_soundtouch._tcp.local.", listener)
"""

if __name__ == '__main__':
        app.run(debug=True)

"""
try:
        input("Press enter to exit...\n\n")
finally:
        zeroconf.close()"""
