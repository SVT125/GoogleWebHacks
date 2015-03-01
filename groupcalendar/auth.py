import httplib2
import argparse
import sys

from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import OAuth2WebServerFlow
import oauth2client.tools 

def create_service():
    flags = oauth2client.tools.argparser.parse_args(args=[]) 
    # Set up a Flow object to be used if we need to authenticate. This
    # sample uses OAuth 2.0, and we set up the OAuth2WebServerFlow with
    # the information it needs to authenticate. Note that it is called
    # the Web Server Flow, but it can also handle the flow for native
    # applications
    # The client_id and client_secret can be found in Google Developers Console
		
    FLOW = OAuth2WebServerFlow(
    client_id='903170588158-hon5hofoumd3b7godo5nvt832f1tmotv.apps.googleusercontent.com',
    client_secret='903170588158-hon5hofoumd3b7godo5nvt832f1tmotv@developer.gserviceaccount.com ',
    scope='https://www.googleapis.com/auth/calendar')

    storage = Storage('calendar.dat')
    credentials = storage.get()
    if credentials is None or credentials.invalid == True:
        credentials = oauth2client.tools.run_flow(FLOW, storage,flags)

    # Create an httplib2.Http object to handle our HTTP requests and authorize it
    # with our good Credentials.
    http = httplib2.Http()
    auth_http = credentials.authorize(http)

    # Build a service object for interacting with the API. Visit
    # the Google Developers Console
    # to get a developerKey for your own application.
    service = build(serviceName='calendar', version='v3', http=http,
           developerKey='AIzaSyC0xnkNlkbj9VVUAY9e7oO0xm8hx-me-q4')
    return service
