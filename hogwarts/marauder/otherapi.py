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
    try:
        hike_bytes = urllib.request.urlopen(os.path.join(twistory, 'api/hikes', web_name)).read()
        hike_dict = json.loads(hike_bytes.decode('utf-8'))
    except Exception:
        print(traceback.format_exc())
        return {'name': 'error', 'time': 'error',
                'distance': 'error', 'park': 'error',
                'image': '#', 'difficulty': 'error'}
    hike_dict['name'] = name
    hike_dict['time'] = hike_dict['est_time(min)']
    hike_dict['distance'] = hike_dict['distance(mile)']
    return hike_dict

def get_park(name):
    '''Get park from name.'''
    web_name = name.replace(' ', '%20')
    try:
        park_bytes = urllib.request.urlopen(os.path.join(twistory, 'api/parks', web_name)).read()
        park_dict = json.loads(park_bytes.decode('utf-8'))
    except Exception:
        print(traceback.format_exc())
        return {'name': 'error', 'max_elevation': 'error',
                'visitors': 'error', 'state': 'error',
                'image': '#'}
    park_dict['name'] = name
    park_dict['max_elevation'] = park_dict['max_elevation(ft)']
    park_dict['visitors'] = park_dict['visitors(annual)']
    return park_dict


