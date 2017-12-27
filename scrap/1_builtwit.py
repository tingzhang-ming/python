from util import *
import builtwith
import json

print json.dumps(builtwith.parse(base_url), indent=5)

"""
{
     "javascript-frameworks": [
          "jQuery", 
          "Modernizr", 
          "jQuery UI"
     ], 
     "web-frameworks": [
          "Web2py", 
          "Twitter Bootstrap"
     ], 
     "programming-languages": [
          "Python"
     ], 
     "web-servers": [
          "Nginx"
     ]
}

"""

import whois   #python-whois

print json.dumps(whois.whois(base_url), indent=5)