from flask import Flask, render_template, request
from six.moves import input

import json
import requests

app = Flask(__name__, template_folder=".")

@app.route('/')
def mainview():
        return render_template('index.html')
    
@app.route('/tripadvisor/')
def trip():
        url = "http://api.tripadvisor.com/api/partner/2.0/map/42.33141,-71.099396/attractions?key=5A21D499D9BD4ECBAEDD8DDA312AB087"
        values = json.loads(requests.get(url).content)
        list = []
        for x in range(0, 5): 
            list.append({'name': values['data'][x]['name'], 'link': values['data'][x]['web_url']})
                
        return render_template('index.html', attractions=list)



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
