# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 16:49:46 2016

@author: Elias Muche 
"""

import http.client
import json 
import dateutil.parser as du
from datetime import datetime, timedelta
#method used for obtaining information,reusable
def getInfo(path,token):
    server.request('POST',path,json.dumps({'token':token}),headers)
    return server.getresponse().read().decode('utf-8')

def sendInfo(path,key,value):
    server.request('POST',path,json.dumps({'token':apiToken,key:value}),headers)
    print(server.getresponse().read())
    
"""
Step 1: Connecting to the api
"""
link='challenge.code2040.org'
apiToken='96307a7534299d7419cc6b634181b9be'
tokenKeys=json.dumps({'token':apiToken,'github':'https://github.com/eliasmuche/Code2040-Challenge'})
headers = {'Content-type': 'application/json'}

try:
   server=http.client.HTTPConnection(link)
   server.request('POST','/api/register',tokenKeys,headers)
   print(server.getresponse().read())
except http.client.HTTPException:   
    print("Couldn't connect to the api")
    
"""
End of step 1
"""
 

"""
Step 2: Obtaining a string, reversing it, and sending it back
"""           
def reverseString(string):
    return string[-1::-1]
       
"""
End of step 2 
"""


"""
Step 3: Finding a needle in a haystack (item in an array)
"""    
def findNeedle(dictionary):
    realDict=json.loads(dictionary)   
    needle=realDict.get('needle')  
    array=realDict.get('haystack')
    for i in range(0,len(array)):
        if array[i]==needle:
            return i
      
"""
End of step 3
"""
 
   
"""
Step 4: Returning an array with elements not beginning with a given prefix
"""
def createPrefixArray(dictionary):
    realDict=json.loads(dictionary)
    pre=realDict.get('prefix')
    array=realDict.get('array')
    myArray=[]
  
    for word in array:
        if len(pre)>len(word) or word[:len(pre)]!=pre:
            myArray.append(word)
    
    return myArray    


"""
End of step 4
"""

"""
Step 5: Adding seconds to a date
"""
def addInterval(date):
    dateDict=json.loads(date) 
    actualDate=du.parse(dateDict.get('datestamp'))
    interval=dateDict.get('interval')  
    actualDate=actualDate + timedelta(seconds=interval) 
    actualDate=actualDate.isoformat()
    array=actualDate.split('+')
    actualDate=array[0]
    actualDate=actualDate + 'Z'
    return actualDate
    
"""
Executing step 2
"""    
reversed=reverseString(getInfo('/api/reverse',apiToken))
sendInfo('/api/reverse/validate','string',reversed)


"""
Executing step 3
"""
dictionary=getInfo('/api/haystack',apiToken)
index=findNeedle(dictionary)
sendInfo('/api/haystack/validate','needle',str(index))
"""
Executing step 4
"""
prefixDict=getInfo('/api/prefix',apiToken)
myArray=createPrefixArray(prefixDict)
sendInfo ('/api/prefix/validate','array',myArray)

"""
Executing step 5
"""
date=getInfo('/api/dating',apiToken)
sendInfo('/api/dating/validate','datestamp',addInterval(date))
