import sys
import urllib2
import json

if __name__=='__main__':
    key=sys.argv[1]
    bus=sys.argv[2]
    print "Bus Line : %s" % bus
    
    #Import API key and bus line number
    url="http://api.prod.obanyc.com/api/siri/vehicle-%%20monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s" % (key, bus)
    request=urllib2.urlopen(url)
    json_file=json.load(request)
    buses=json_file['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

    print "Number of Active Buses : %d" % len(buses)
    for i in range(len(buses)):
        location=buses[i]['MonitoredVehicleJourney']["VehicleLocation"]
        latitude=location['Latitude']
        longitude=location['Longitude']
        print "Bus %d is at latitude %f and longtitude %f" % (i, latitude, longitude)
