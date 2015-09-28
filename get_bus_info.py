import sys
import urllib2
import json
import csv

if __name__=='__main__':
    key=sys.argv[1]
    bus=sys.argv[2]
    print "Bus Line : %s" % bus

    #Code for using API key to get particular bus line info                                                                                                                                             
    url="http://api.prod.obanyc.com/api/siri/vehicle-%%20monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s" % (key, bus)
    request=urllib2.urlopen(url)
    json_file=json.load(request)
    buses=json_file['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

    print "Number of Active Buses : %d" % len(buses)

    #Error occurred in this part. I kept getting list index out of range error from next line. However, after I changed sys.argv[3] to sys.argv[2], the program worked but could not generate a csv fil\
e. It did create a text file with all the information.                                                                                                                                                  
    with open(sys.argv[2],'wb') as csvfile:
        writer=csv.writer(csvfile, delimiter=',')
        writer.writerow(['Latitude', 'Longitude', 'Stop Name', 'Stop Status' ])
        for i in range(len(buses)):
            bus=buses[i]['MonitoredVehicleJourney']
            latitude=bus['VehicleLocation']['Latitude']
            longitude=bus['VehicleLocation']['Longitude']
            if bus['OnwardCalls']=={}:
                stop_name='NA'
                stop_dis='NA'
            else:
                stop_name=bus['MonitoredCall']['StopPointName']
                stop_dist=bus['OnwardCalls']['OnwardCall'][0]['Extensions']["Distances"]['PresentableDistance']
            writer.writerow([latitude, longitude, stop_name, stop_dist])
