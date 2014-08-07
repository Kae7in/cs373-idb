#!/usr/bin/env python3
import os
import urllib3.request
import json
import traceback

twistory = 'http://twistory.pythonanywhere.com'

def get_json(url):
    print("URL: " + str(url))
    http = urllib3.PoolManager()
    data = http.request('GET', url).data
    return json.loads(data.decode('utf-8'))

def get_parks():
    '''Get list of all parks.'''
    parks = get_json(os.path.join(twistory, 'api/parks'))
    return [k for k in parks.keys()]

def get_hikes():
    '''Get list of hikes in list of strenuous, middle, easy.'''
    hikes = get_json(os.path.join(twistory, 'api/hikes'))
    difficult = []
    moderate = []
    easy = []

    for key in hikes:
        hike = get_json(os.path.join(twistory, 'api/hikes', key))
        if hike['difficulty'].lower() == 'strenuous':
            difficult.append(key)
        elif hike['difficulty'].lower() == 'moderate':
            moderate.append(key)
        elif hike['difficulty'].lower() == 'easy':
            easy.append(key)
    return difficult, moderate, easy

def get_hike(name):
    '''Get hike from name.'''
    web_name = name.replace(' ', '%20')
    hike = get_json(os.path.join(twistory, 'api/hikes', web_name))
    hike['name'] = name
    hike['time'] = hike['est_time(min)']
    hike['distance'] = hike['distance(mile)']
    return hike

def get_park(name):
    '''Get park from name.'''
    web_name = name.replace(' ', '%20')
    park = get_json(os.path.join(twistory, 'api/parks', web_name))
    park['name'] = name
    park['max_elevation'] = park['max_elevation(ft)']
    park['visitors'] = park['visitors(annual)']
    return park


