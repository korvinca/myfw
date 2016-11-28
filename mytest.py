'''
Created on Oct 19, 2016
Create a new python module, called mytest.py and write all test code (calls etc) for these functions
Use a mySQL DB and local apache server for all

@author: sashaalexander
@author: team 2
'''

import sys
from rfaUtils import getLocalEnv, getDbConnection, getDbCursor, queryDb, check_ping
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
ping = check_ping(server_url)
if ping == -1:
    sys.exit("[ERROR] Network Error")

connector = getDbConnection(server_url, db_name, db_user, db_pass)
if connector == -1:
    sys.exit("[ERROR] Connect to DB failed")

# get cursor
cursor = getDbCursor(connector)
if cursor == -1:
    sys.exit("[ERROR] Getting cursor failed")

# select something from db
queryDb(cursor)

# get response
url = buildURL(list_str)[0]
if server_port == "80":
    url = "http://" + url
else:
    url = "https://" + url
response = getHttpResponse(url, method, parameters)
if response == -1:
    sys.exit("[ERROR] Getting response from URL failed")

# get response code
stringCode = getHttpResponseCode(response, 'string')
if stringCode == -1:
    sys.exit("[ERROR] Getting stringCode failed")
print response, type(stringCode)
intCode = getHttpResponseCode(response, 'int')
if stringCode == -1:
    sys.exit("[ERROR] Getting stringCode failed")
print response, type(intCode)

# close connection
cursor.close()