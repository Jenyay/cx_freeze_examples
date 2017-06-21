# coding: utf-8

import json


if __name__ == '__main__':
    fname = 'data/data.json'
    with open(fname) as fp:
        obj = json.load(fp)

    print('Hello {} {}!'.format(obj['first_name'], obj['last_name']))
