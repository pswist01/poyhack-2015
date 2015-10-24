from flask import Flask, render_template, request
from zeroconf import ServiceBrowser, Zeroconf
from six.moves import input
import random
"""from flask.ext.googlemaps import GoogleMaps
from flask.ext.googlemaps import Map"""

import json
import requests

app = Flask(__name__, template_folder=".")
"""GoogleMaps(app)"""

@app.route('/')
def mainview():
        return render_template('index.html')
    

@app.route('/kicked/', defaults={'lat': 42.33141, 'lon': -71.099396})
@app.route('/kicked/<lat>&<lon>')
def trip(lat, lon):
        """lat = 42.33141
        lon = -71.099396"""

        url = "http://api.tripadvisor.com/api/partner/2.0/map/" + str(lat) \
            + "," + str(lon) + "/attractions?key=5A21D499D9BD4ECBAEDD8DDA312AB087"

        values = json.loads(requests.get(url).content)
        list = []
        alreadyUsed = []
        numAttractions = 6
        for x in range(0, numAttractions): 
            while True:
                i = random.randrange(0, len(values['data']))
                if (i not in alreadyUsed):
                    alreadyUsed.append(i)
                    break
            list.append({'name': values['data'][i]['name'], 
                'link': values['data'][i]['web_url'],
                'rating': str(values['data'][i]['rating'])})
                
        return render_template('kicked.html', attractions=list)



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
