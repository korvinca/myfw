'''
Created on Oct 19, 2016
Create a new python module, called mytest.py and write all test code (calls etc) for these functions
Use a mySQL DB and local apache server for all

@author: sashaalexander
@author: team 2
'''

import sys
from rfaUtils import getLocalEnv, getDbConnection, getDbCursor, queryDb
from rfaUtils import buildURL, getHttpResponse, getHttpResponseCode

# read properties
localProperties = getLocalEnv('local.properties')
if localProperties == -1:
    sys.exit('[ERROR]Could not read properties')
server_url = localProperties['test_server_URL']
server_port = localProperties['test_server_port']
db_port = localProperties['test_db_port']
db_user = localProperties['db_user']
db_pass = localProperties['db_pass']
db_name = "bugs"
list_str = [server_url, "/", "/auth/whoami"]
method = 'get'
parameters = {"username": "user_name", "password": "user_password"}
# get connector
connector = getDbConnection(server_url, db_name, db_user, db_pass)
# get cursor
cursor = getDbCursor(connector)
# select something from db
queryDb(cursor)
# get response
url = buildURL(list_str)[0]
if server_port == "80":
    url = "http://" + url
else:
    url = "https://" + url
response = getHttpResponse(url, method, parameters)
# get response code
stringCode = getHttpResponseCode(response, 'string')
print response, type(stringCode)
intCode = getHttpResponseCode(response, 'int')
print response, type(intCode)