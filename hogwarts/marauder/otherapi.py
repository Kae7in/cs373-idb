#!/usr/bin/env python3
import os
import urllib.request
import json
import traceback

twistory = 'http://twistory.pythonanywhere.com'

def get_parks():
    '''Get list of all parks.'''
    try:
        parks_bytes = urllib.request.urlopen(os.path.join(twistory, 'api/parks')).read()
        parks_dict = json.loads(parks_bytes.decode('utf-8'))
        return [k for k in parks_dict.keys()]
    except Exception:
        return None

def get_hikes():
    '''Get list of hikes in list of strenuous, middle, easy.'''

    hikes_bytes = urllib.request.urlopen(os.path.join(twistory, 'api/hikes')).read()
    hikes_dict = json.loads(hikes_bytes.decode('utf-8'))
    difficult = []
    moderate = []
    easy = []
    for key in hikes_dict:
        try:
            hike_bytes = urllib.request.urlopen(os.path.join(twistory, 'api/hikes', key)).read()
            hike_dict = json.loads(hike_bytes.decode('utf-8'))
            if hike_dict['difficulty'].lower() == 'strenuous':
                difficult.append(key)
            elif hike_dict['difficulty'].lower() == 'moderate':
                moderate.append(key)
            elif hike_dict['difficulty'].lower() == 'easy':
                easy.append(key)
        except Exception:
            continue
    return difficult, moderate, easy

def get_hike(name):
    '''Get hike from name.'''
    web_name = name.replace(' ', '%20')
    hike_bytes = urllib.request.urlopen(os.path.join(twistory, 'api/hikes', web_name)).read()
    hike_dict = json.loads(hike_bytes.decode('utf-8'))
    hike_dict['name'] = name
    hike_dict['time'] = hike_dict['est_time(min)']
    hike_dict['distance'] = hike_dict['distance(mile)']
    return hike_dict

