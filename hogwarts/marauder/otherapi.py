#!/usr/bin/env python3
import os
import urllib3.request
import json
import traceback

twistory = 'http://twistory.pythonanywhere.com'

def get_json(url):
    try:
        http = urllib3.PoolManager()
        data = http.request('GET', url).data
        return json.loads(data.decode('utf-8'))
    except Exception:
        return None

def get_parks():
    '''Get list of all parks.'''
    try:
        parks = get_json(os.path.join(twistory, 'api/parks'))
        return [k for k in parks.keys()]
    except Exception:
        return None

def get_hikes(just_one):
    '''Get list of hikes in list of strenuous, middle, easy.'''
    try:
        hikes = get_json(os.path.join(twistory, 'api/hikes'))
        difficult = []
        moderate = []
        easy = []

        for key in hikes:
            try:
                hike = get_json(os.path.join(twistory, 'api/hikes', key))
                if hike['difficulty'].lower() == 'strenuous':
                    difficult.append(key)
                elif hike['difficulty'].lower() == 'moderate':
                    moderate.append(key)
                elif hike['difficulty'].lower() == 'easy':
                    easy.append(key)
                if(just_one and len(difficult) >= 1 and len(moderate) >= 1 and len(easy) >= 1):
                    break
            except MaxRetryError:
                pass
        return difficult, moderate, easy
    except Exception:
        return None

def get_one_hike_for_each_difficulty():
    hikes = get_hikes(True)
    if(hikes is None):
        return (None, None, None)

    difficult, moderate, easy = hikes
    difficult = get_json(os.path.join(twistory, 'api/hikes', difficult.pop()))
    moderate = get_json(os.path.join(twistory, 'api/hikes', moderate.pop()))
    easy = get_json(os.path.join(twistory, 'api/hikes', easy.pop()))
    return difficult, moderate, easy

def get_hike(name):
    '''Get hike from name.'''
    try:
        web_name = name.replace(' ', '%20')
        hike = get_json(os.path.join(twistory, 'api/hikes', web_name))
        hike['name'] = name
        hike['time'] = hike['est_time(min)']
        hike['distance'] = hike['distance(mile)']
        return hike
    except Exception:
        return None

def get_park(name):
    '''Get park from name.'''
    try:
        web_name = name.replace(' ', '%20')
        park = get_json(os.path.join(twistory, 'api/parks', web_name))
        park['name'] = name
        park['max_elevation'] = park['max_elevation(ft)']
        park['visitors'] = park['visitors(annual)']
        return park
    except Exception:
        return None


