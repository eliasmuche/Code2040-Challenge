# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 16:49:46 2016

@author: Elias Muche 
"""

import http.client
import json 

link='challenge.code2040.org'
apiToken='96307a7534299d7419cc6b634181b9be'
tokenKeys=json.dumps({'token':apiToken,'github':'https://github.com/eliasmuche/Code2040-Challenge'})
headers = {'Content-type': 'application/json'}


try:
    
   server=http.client.HTTPConnection(link)
   server.request('POST','/api/register',tokenKeys,headers)
   status=server.getresponse()
   status.read()
 
      
except http.client.HTTPException:   
    print("Couldn't connect to the api")

def reverseString(string):
    return string[-1::-1]
    
    
def sendReversed(reverse,path,token):
    server.request('POST',path,json.dumps({'token':token,'string':reverse}),headers)
    server.getresponse().read() 

def getInfo(path,token):
    server.request('POST',path,json.dumps({'token':token}),headers)
    return server.getresponse().read().decode('utf-8')
    
def findNeedle(dictionary):
    realDict=json.loads(dictionary)   
    needle=realDict.get('needle')  
    array=realDict.get('haystack')
    for i in range(0,len(array)):
        if array[i]==needle:
            return i
       

def sendNeedleLocation(needleIndex,path):
    server.request('POST',path,json.dumps({'token':apiToken,'needle':str(needleIndex)}),headers)
    server.getresponse().read()
    
    
reversed=reverseString(getInfo('/api/reverse',apiToken))
sendReversed(reversed,'/api/reverse/validate',apiToken)
dictionary=getInfo('/api/haystack',apiToken)

index=findNeedle(dictionary)
sendNeedleLocation(index,'/api/haystack/validate')



