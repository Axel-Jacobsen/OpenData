"""
Prints and saves bridge traffic speed/direction data from translink API.
In future, hope to incorporate a system where one would be able
    a) to send a text message requesting traffic data on LGB
    b) to send text messages reqesting traffic data for different lower mainalnd locations
    c) to be able to incorporate multiple people at once (i.e. someone else can send a text message and get the data back

"""

import time
import urllib.request
import json

# Formatting csv file (if you already have a csv file, omit this code)
"""
with open('dayfile.csv', 'w') as today:
    today.write('Time (UTC), Northbound, Southbound\n')
"""

while True:

    # Get the data for Norf side of lions gate bridge
    u = urllib.request.urlopen('https://rtdsapi.translink.ca/rtdsapi/v1/LiveDataAtPoint?apikey=l9AKRy9Fuj2MNtBGOkZb&x=-123.130078&y=49.32477&z=10&types=3')
    lions_gate_data = u.read().decode('utf-8')
    with open('lions_gate_file.txt', 'w') as lions_gate_file:
        lions_gate_file.write(lions_gate_data)

    # Parses and prints the speed and direction at North Face of lions gate
    with open('lions_gate_file.txt', 'r') as lions_gate_file:

        # Next 4 lines are pulling the data from lions_gate_file, and formating it
        # for next steps
        file_data = lions_gate_file.read()
        file_parsed = json.loads(file_data)
        data = file_parsed["data"]
        fordatafile = str(file_parsed['timestampUtc']) + ',' + str(data[0]['speedKmph']) + ',' + str(data[1]['speedKmph']) + '\n'

        # Writes data every 2.5 minutes to file
        with open('dayfile.csv', 'a') as today:
            today.write(fordatafile)

        # Prints data to terminal
        print(" North bound: ", data[0]['speedKmph'], 'km/h \n', "South bound: ", data[1]['speedKmph'], 'km/h \n')

    # Wait 2.5 minutes (refresh time of data file)
    time.sleep(60*2.5)

