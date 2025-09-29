# STEP 4 - INITIAL REQUEST

import requests

token = "81fb791c686ee1a615e96b00aa157e6f186d216c"  
url = "https://api.waqi.info/search/"
response = requests.get(url, params={"token": token, "keyword": "montreal"})
results = response.json()
# print(results)  # show full results


#-------------------------------------------------------------------------


# STEP 5 - EXPLORING THE RESULTS

print(type(results))
#Q: What type is results?
#A: <class 'dict'>

print(results.keys())
#Q: What keys does results have?
#A: dict_keys(['status', 'data'])

responseData = results["data"]
print(type(responseData))
#Q: What type is responseData?
#A: <class 'list'> (a list of monitoring station dictionaries)

for item in responseData:
    print(item)
#Q: What does each item represent?
#A: each item is one station's info (dictionary)
#{'uid': 5922, 'aqi': '33', 'time': {'tz': '-04:00', 'stime': '2025-09-28 23:00:00', 'vtime': 1759114800}, 'station': {'name': 'Montreal', 'geo': [45.5086699, -73.5539925], 'url': 'montreal'}}
#{'uid': 8695, 'aqi': '35', 'time': {'tz': '-04:00', 'stime': '2025-09-27 23:00:00', 'vtime': 1759028400}, 'station': {'name': 'Jardin Botanique, Montreal, Canada', 'geo': [45.56221, -73.571785], 'url': 'canada/montreal/jardin-botanique', 'country': 'CA'}}
#{'uid': 5467, 'aqi': '33', 'time': {'tz': '-04:00', 'stime': '2025-09-28 23:00:00', 'vtime': 1759114800}, 'station': {'name': 'Molson, Montreal, Canada', 'geo': [45.542767, -73.572039], 'url': 'canada/montreal/molson', 'country': 'CA'}}
#{'uid': 5463, 'aqi': '30', 'time': {'tz': '-04:00', 'stime': '2025-09-28 23:00:00', 'vtime': 1759114800}, 'station': {'name': 'Hochelaga-Maisonneuve, Montreal, Canada', 'geo': [45.539928, -73.540388], 'url': 'canada/montreal/hochelaga-maisonneuve', 'country': 'CA'}}
#{'uid': 5461, 'aqi': '30', 'time': {'tz': '-04:00', 'stime': '2025-09-28 23:00:00', 'vtime': 1759114800}, 'station': {'name': 'Caserne 17, Montreal, Canada', 'geo': [45.593325, -73.637328], 'url': 'canada/montreal/caserne-17', 'country': 'CA'}}
#{'uid': 8595, 'aqi': '27', 'time': {'tz': '-04:00', 'stime': '2025-09-28 23:00:00', 'vtime': 1759114800}, 'station': {'name': 'Échangeur Décarie, Montreal, Canada', 'geo': [45.502648, -73.663913], 'url': 'canada/montreal/echangeur-decarie', 'country': 'CA'}}
#{'uid': 10138, 'aqi': '21', 'time': {'tz': '-04:00', 'stime': '2025-09-28 23:00:00', 'vtime': 1759114800}, 'station': {'name': 'St-Dominique, Montreal, Canada', 'geo': [45.512189, -73.566842], 'url': 'canada/montreal/st-dominique', 'country': 'CA'}}
#{'uid': 8594, 'aqi': '21', 'time': {'tz': '-04:00', 'stime': '2025-09-28 17:00:00', 'vtime': 1759093200}, 'station': {'name': 'Verdun, Montreal, Canada', 'geo': [45.472854, -73.57296], 'url': 'canada/montreal/verdun', 'country': 'CA'}}
#{'uid': 8696, 'aqi': '18', 'time': {'tz': '-04:00', 'stime': '2025-09-28 23:00:00', 'vtime': 1759114800}, 'station': {'name': 'Saint-Michel, Montreal, Canada', 'geo': [45.563697, -73.610447], 'url': 'canada/montreal/saint-michel', 'country': 'CA'}}
#{'uid': 5465, 'aqi': '18', 'time': {'tz': '-04:00', 'stime': '2025-09-28 20:00:00', 'vtime': 1759104000}, 'station': {'name': 'Maisonneuve, Montreal, Canada', 'geo': [45.501531, -73.574311], 'url': 'canada/montreal/maisonneuve', 'country': 'CA'}}
#{'uid': 8626, 'aqi': '18', 'time': {'tz': '-04:00', 'stime': '2025-09-28 18:00:00', 'vtime': 1759096800}, 'station': {'name': 'Drummond, Montreal, Canada', 'geo': [45.497859, -73.573035], 'url': 'canada/montreal/drummond', 'country': 'CA'}}
#{'uid': 10716, 'aqi': '18', 'time': {'tz': '-04:00', 'stime': '2025-09-28 18:00:00', 'vtime': 1759096800}, 'station': {'name': 'Roberval, York, Montreal, Canada', 'geo': [45.464611, -73.582583], 'url': 'canada/montreal/york/roberval', 'country': 'CA'}}
#{'uid': 8596, 'aqi': '-', 'time': {'tz': '-04:00', 'stime': '2025-09-26 23:00:00', 'vtime': 1758942000}, 'station': {'name': 'Parc Pilon, Montreal, Canada', 'geo': [45.594576, -73.641535], 'url': 'canada/montreal/parc-pilon', 'country': 'CA'}}
#{'uid': 8628, 'aqi': '-', 'time': {'tz': '-04:00', 'stime': '2025-09-26 22:00:00', 'vtime': 1758938400}, 'station': {'name': 'Ontario, Montreal, Canada', 'geo': [45.52055, -73.563222], 'url': 'canada/montreal/ontario', 'country': 'CA'}}
#{'uid': 5462, 'aqi': '-', 'time': {'tz': '-04:00', 'stime': '1970-01-01 00:00:00', 'vtime': 0}, 'station': {'name': 'Duncan, Montreal, Canada', 'geo': [45.4660102, -73.6336838], 'url': 'canada/montreal/duncan', 'country': 'CA'}}
#{'uid': 8625, 'aqi': '33', 'time': {'tz': '-04:00', 'stime': '2025-09-28 23:00:00', 'vtime': 1759114800}, 'station': {'name': 'Anjou, Montreal, Canada', 'geo': [45.602846, -73.558874], 'url': 'canada/montreal/anjou'}}
#{'uid': 8627, 'aqi': '21', 'time': {'tz': '-04:00', 'stime': '2025-09-28 14:00:00', 'vtime': 1759082400}, 'station': {'name': 'Dorval, Montreal, Canada', 'geo': [45.439119, -73.7333], 'url': 'canada/montreal/dorval'}}
#{'uid': 5460, 'aqi': '18', 'time': {'tz': '-04:00', 'stime': '2025-09-28 18:00:00', 'vtime': 1759096800}, 'station': {'name': 'Chénier, Montreal, Canada', 'geo': [45.60176, -73.541992], 'url': 'canada/montreal/chenier'}}
#{'uid': 5459, 'aqi': '30', 'time': {'tz': '-04:00', 'stime': '2025-09-28 23:00:00', 'vtime': 1759114800}, 'station': {'name': 'Saint-Jean-Baptiste, Montreal, Canada', 'geo': [45.641026, -73.499682], 'url': 'canada/montreal/saint-jean-baptiste'}}
#{'uid': 5466, 'aqi': '21', 'time': {'tz': '-04:00', 'stime': '2025-09-28 23:00:00', 'vtime': 1759114800}, 'station': {'name': 'Aéroport de Montréal, Montreal, Canada', 'geo': [45.468297, -73.741185], 'url': 'canada/montreal/aeroport-de-montreal'}}
#{'uid': 5468, 'aqi': '18', 'time': {'tz': '-04:00', 'stime': '2025-09-28 23:00:00', 'vtime': 1759114800}, 'station': {'name': 'Sainte-Anne-de-Bellevue, Montreal, Canada', 'geo': [45.426509, -73.928944], 'url': 'canada/montreal/sainte-anne-de-bellevue'}}

print(type(item))
#Q: What type is item?
#A: <class 'dict'>

print(item.keys())
#Q: What keys does each item have?
#A: dict_keys(['uid', 'aqi', 'time', 'station'])

for item in responseData:
    print("Station:", item["station"]["name"])
#Q: What station names do we get?
#A: Station: Montreal
#Station: Jardin Botanique, Montreal, Canada
#Station: Molson, Montreal, Canada
#Station: Hochelaga-Maisonneuve, Montreal, Canada
#Station: Caserne 17, Montreal, Canada
#Station: Échangeur Décarie, Montreal, Canada
#Station: St-Dominique, Montreal, Canada
#Station: Verdun, Montreal, Canada
#Station: Saint-Michel, Montreal, Canada
#Station: Maisonneuve, Montreal, Canada
#Station: Drummond, Montreal, Canada
#Station: Roberval, York, Montreal, Canada
#Station: Parc Pilon, Montreal, Canada
#Station: Ontario, Montreal, Canada
#Station: Duncan, Montreal, Canada
#Station: Anjou, Montreal, Canada
#Station: Dorval, Montreal, Canada
#Station: Chénier, Montreal, Canada
#Station: Saint-Jean-Baptiste, Montreal, Canada
#Station: Aéroport de Montréal, Montreal, Canada
#Station: Sainte-Anne-de-Bellevue, Montreal, Canada

for item in responseData:
    lat = item["station"]["geo"][0]
    lon = item["station"]["geo"][1]
    print("lat:", lat)
    print("long:", lon)
#Q: What are the geolocations?
#A:lat: 45.5086699
#long: -73.5539925
#lat: 45.56221
#long: -73.571785
#lat: 45.542767
#long: -73.572039
#lat: 45.539928
#long: -73.540388
#lat: 45.593325
#long: -73.637328
#lat: 45.502648
#long: -73.663913
#lat: 45.512189
#long: -73.566842
#lat: 45.472854
#long: -73.57296
#lat: 45.563697
#long: -73.610447
#lat: 45.501531
#long: -73.574311
#lat: 45.497859
#long: -73.573035
#lat: 45.464611
#long: -73.582583
#lat: 45.594576
#long: -73.641535
#lat: 45.52055
#long: -73.563222
#lat: 45.4660102
#long: -73.6336838
#lat: 45.602846
#long: -73.558874
#lat: 45.439119
#long: -73.7333
#lat: 45.60176
#long: -73.541992
#lat: 45.641026
#long: -73.499682
#lat: 45.468297
#long: -73.741185
#lat: 45.426509
#long: -73.928944

for item in responseData:
    print("Station:", item["station"]["name"])
    print("AQI:", item["aqi"])
    print("UID:", item["uid"])
    print("------")
#Q: What AQI and UID values do we get? 
#A: Station: Montreal
#AQI: 33
#UID: 5922
#------
#Station: Jardin Botanique, Montreal, Canada
#AQI: 35
#UID: 8695
#------
#Station: Molson, Montreal, Canada
#AQI: 33
#UID: 5467
#------
#Station: Hochelaga-Maisonneuve, Montreal, Canada
#AQI: 30
#UID: 5463
#------
#Station: Caserne 17, Montreal, Canada
#AQI: 30
#UID: 5461
#------
#Station: Échangeur Décarie, Montreal, Canada
#AQI: 27
#UID: 8595
#------
#Station: St-Dominique, Montreal, Canada
#AQI: 21
#UID: 10138
#------
#Station: Verdun, Montreal, Canada
#AQI: 21
#UID: 8594
#------
#AQI: 18
#UID: 8696
#------
#Station: Maisonneuve, Montreal, Canada
#AQI: 18
#UID: 5465
#------
#Station: Drummond, Montreal, Canada
#AQI: 18
#UID: 8626
#------
#Station: Roberval, York, Montreal, Canada
#AQI: 18
#UID: 10716
#------
#Station: Parc Pilon, Montreal, Canada
#AQI: -
#UID: 8596
#------
#Station: Ontario, Montreal, Canada
#AQI: -
#UID: 8628
#------
#Station: Duncan, Montreal, Canada
#AQI: -
#UID: 5462
#------
#Station: Anjou, Montreal, Canada
#AQI: 33
#UID: 8625
#------
#Station: Dorval, Montreal, Canada
#AQI: 21
#UID: 8627
#------
#Station: Chénier, Montreal, Canada
#AQI: 18
#UID: 5460
#------
#Station: Saint-Jean-Baptiste, Montreal, Canada
#AQI: 30
#UID: 5459
#------
#Station: Aéroport de Montréal, Montreal, Canada
#AQI: 21
#UID: 5466
#------
#Station: Sainte-Anne-de-Bellevue, Montreal, Canada
#AQI: 21
#UID: 5468
#------


#-------------------------------------------------------------------------


#STEP 6 - FEED REQUEST

url_feed = "https://api.waqi.info/feed/@5468"  
response_feed = requests.get(url_feed, params={"token": token})
results_feed = response_feed.json()
print(results_feed)
#Q: What does results_feed look like?
#A: {'status': 'ok', 'data': {'aqi': 21, 'idx': 5468, 'attributions': [{'url': 'http://ville.montreal.qc.ca/portal/page?_pageid=7237,74495616&_dad=portal&_schema=PORTAL', 'name': "Ville de Montreal - Réseau de surveillance de la qualité de l'air", 'logo': 'Canada-Montreal.png'}, {'url': 'https://waqi.info/', 'name': 'World Air Quality Index Project'}], 'city': {'geo': [45.426509, -73.928944], 'name': 'Sainte-Anne-de-Bellevue, Montreal, Canada', 'url': 'https://aqicn.org/city/canada/montreal/sainte-anne-de-bellevue', 'location': ''}, 'dominentpol': 'pm25', 'iaqi': {'co': {'v': 6.4}, 'dew': {'v': 8}, 'h': {'v': 67}, 'no2': {'v': 3.7}, 'o3': {'v': 14}, 'pm25': {'v': 21}, 'so2': {'v': 5.1}, 't': {'v': 14}, 'w': {'v': 3.6}, 'wg': {'v': 8.2}}, 'time': {'s': '2025-09-29 00:00:00', 'tz': '-04:00', 'v': 1759104000, 'iso': '2025-09-29T00:00:00-04:00'}, 'forecast': {'daily': {'pm10': [{'avg': 7, 'day': '2025-09-27', 'max': 9, 'min': 3}, {'avg': 10, 'day': '2025-09-28', 'max': 17, 'min': 5}, {'avg': 6, 'day': '2025-09-29', 'max': 10, 'min': 4}, {'avg': 6, 'day': '2025-09-30', 'max': 9, 'min': 3}, {'avg': 6, 'day': '2025-10-01', 'max': 12, 'min': 4}, {'avg': 8, 'day': '2025-10-02', 'max': 14, 'min': 4}, {'avg': 9, 'day': '2025-10-03', 'max': 14, 'min': 5}], 'pm25': [{'avg': 18, 'day': '2025-09-27', 'max': 30, 'min': 10}, {'avg': 35, 'day': '2025-09-28', 'max': 56, 'min': 17}, {'avg': 18, 'day': '2025-09-29', 'max': 25, 'min': 14}, {'avg': 13, 'day': '2025-09-30', 'max': 24, 'min': 7}, {'avg': 14, 'day': '2025-10-01', 'max': 28, 'min': 7}, {'avg': 18, 'day': '2025-10-02', 'max': 30, 'min': 8}, {'avg': 30, 'day': '2025-10-03', 'max': 52, 'min': 18}], 'uvi': [{'avg': 1, 'day': '2025-09-28', 'max': 5, 'min': 0}, {'avg': 1, 'day': '2025-09-29', 'max': 5, 'min': 0}, {'avg': 1, 'day': '2025-09-30', 'max': 5, 'min': 0}, {'avg': 1, 'day': '2025-10-01', 'max': 4, 'min': 0}, {'avg': 1, 'day': '2025-10-02', 'max': 5, 'min': 0}, {'avg': 0, 'day': '2025-10-03', 'max': 0, 'min': 0}]}}, 'debug': {'sync': '2025-09-29T14:40:55+09:00'}}}

response_data_feed = results_feed["data"]
print(type(response_data_feed))
#Q: What type is response_data_feed?
#A: <class 'dict'>

for key in response_data_feed:
    print(key)
#Q: What keys are in response_data_feed?
#A: aqi
#idx
#attributions
#city
#dominentpol
#iaqi
#time
#forecast
#debug

aqi = response_data_feed["aqi"]
dominentpol = response_data_feed["dominentpol"]
print("AQI:", aqi)
print("Dominant pollutant:", dominentpol)
#Q: What is the AQI and dominentpol?
#A: AQI: 21
#Dominant pollutant: pm25

iaqi = response_data_feed["iaqi"]
print(iaqi.keys())
#Q: What pollutants are listed in iaqi?
#A: dict_keys(['co', 'dew', 'h', 'no2', 'o3', 'pm25', 'so2', 't', 'w', 'wg'])

for pollutant in iaqi:
    print(pollutant, ":", iaqi[pollutant]["v"])
#Q: What are the pollutant values?
#A: co : 6.4
#dew : 8
#h : 67
#no2 : 3.7
#o3 : 14
#pm25 : 21
#so2 : 5.1
#t : 14
#w : 3.6
#wg : 8.2

dominant_value = iaqi[dominentpol]["v"]
print("Dominant pollutant value:", dominant_value)
#Q: What is the value of the dominant pollutant?
#A: Dominant pollutant value: 21


#-------------------------------------------------------------------------


# STEP 7 - THEORETICAL EXPLANATION
#
# The overall process would look like this:
#
# 1. Start with the /search endpoint and provide a keyword for the city you want. 
#    This gives back a list of monitoring stations, each with its own UID.
#
# 2. From this list, pick one or more UIDs. Each UID represents one station.
#
# 3. For every UID, make a new request to the /feed/@UID endpoint. 
#    The "@UID" part tells the API which station we are asking about.
#
# 4. From the feed response, look at the "dominentpol" field to find out which 
#    pollutant is considered the most important at that station.
#
# 5. Use the "dominentpol" value as a key inside the "iaqi" dictionary to get the 
#    actual number (stored under "v") for that pollutant.
#
# 6. Repeat this process for as many stations or cities as needed, collecting all 
#    the dominant pollutant values you want.
#
# In short: search -> get UIDs -> feed request -> find dominentpol -> use iaqi 
# to get the value. This same pattern could be applied across multiple cities.
