# -*- coding: utf-8 -*-

import requests

s = requests.session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r = s.get('https://httpbin.org/cookies', verify=False)
print(r.text)
