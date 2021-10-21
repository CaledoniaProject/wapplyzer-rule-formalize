#!/usr/bin/env python3
# https://github.com/AliasIO/wappalyzer/blob/master/README.md

import os
import json
import requests

base_repo = 'https://raw.githubusercontent.com/AliasIO/wappalyzer/master'

def download_file(url):
    print('Fetching ' + url)

    resp = requests.get(url)
    return resp.text

def save_local(data, filename):
    with open(filename, 'w') as f:
        f.write(data)

def load_from_local():
    cats  = {}
    techs = []

    with open('technologies.json', 'r') as f:
        cats = f.read()
        cats = json.loads(cats)
   
    with open('technologies.json', 'r') as f:
        techs = f.read()
        techs = json.loads(techs)

    return cats, techs

def load_from_network():
    cats  = {}
    techs = {}

    cats = download_file(base_repo + '/src/categories.json')

    for key in list('_abcdefghijklmnopqrstuvwxyz'):
        data  = download_file(base_repo + '/src/technologies/{0}.json'.format(key))
        data  = json.loads(data)
        techs = techs | data

    return cats, techs

def flattern_data(cats, techs):
    result = []

    for key, value in techs.items():
        tmp = value
        value['name'] = key

        if 'dom' in value:
            if isinstance(value['dom'], list):
                value['dom'] = {
                    '__raw_content': value['dom']
                }
            elif isinstance(value['dom'], str):
                value['dom'] = {
                    '__raw_content': [value['dom']]
                }

        for field in ['dns', 'meta']:
            if field not in value:
                continue
            
            tmp = value[field]
            for key2, value2 in tmp.items():
                if isinstance(value2, str):
                    tmp[key2] = [value2]

            value[field] = tmp

        for field in ['xhr', 'implies', 'requires', 'excludes', 'html', 'css', 'robots', 'scriptSrc', 'scripts']:
            if field not in value:
                continue
            
            if isinstance(value[field], str):
                value[field] = [value[field]]
            elif not isinstance(value[field], list):
                raise Exception("Unexpected data type", value)

        result.append(value)

    return result

if __name__ == '__main__':
    cats, techs = load_from_network()
    result = flattern_data(cats, techs)
    save_local(json.dumps(result), 'tech.json')
