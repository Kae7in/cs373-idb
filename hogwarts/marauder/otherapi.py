#!/usr/bin/env python3
import os
import urllib.request
import json
import traceback
'''
Muggle Destinations
Where should I go? 

1. I want the most extreme adventure ever (Forbidden Forest).
2. I just want to wander around with friends (Hogsmeade).
3. I am bringing my parents (Diagon Alley).

(Climate - winter, desert)
1.  

Result: List of destinations with hyperlink 
Hyperlink to twistory destination (Park, Hike)

'''
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
