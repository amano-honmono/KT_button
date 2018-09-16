# -*- coding: utf-8 -*-

import redis
redis = redis.Redis(host='localhost', port=6379)

def top():
    keys = sorted(redis.keys())
    res = ''
    for key in keys:
        s = '<p>%s %s</p>' % (key.decode('utf-8'), redis.get(key).decode('utf-8'))
        res += s
    print(res) #debug
    return res
