# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 16:49:46 2016

@author: Elias
"""

import http.client
import json 

link='challenge.code2040.org'
apiToken='96307a7534299d7419cc6b634181b9be'
tokenKeys=json.dumps({'token':apiToken,'github':'https://github.com/eliasmuche/Code2040-Challenge'})
headers = {'Content-type': 'application/json'}

def connectToApi():
    try:
    
        server=http.client.HTTPConnection(link)
        server.request('POST','/api/register',tokenKeys,headers)
        status=server.getresponse()
        print(status)
        
    except http.client.HTTPException:   
        print("There was a problem")

def reverseString(string):
    return string[-1::-1]

connectToApi()