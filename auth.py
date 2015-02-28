import gflags
import httplib2

from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.tools import run

def create_service() -> 'service':
    FLAGS = gflags.FLAGS

    # Set up a Flow object to be used if we need to authenticate. This
    # sample uses OAuth 2.0, and we set up the OAuth2WebServerFlow with
    # the information it needs to authenticate. Note that it is called
    # the Web Server Flow, but it can also handle the flow for native
    # applications
    # The client_id and client_secret can be found in Google Developers Console
    FLOW = OAuth2WebServerFlow(
        client_id='903170588158-hon5hofoumd3b7godo5nvt832f1tmotv.apps.googleusercontent.com',
        client_secret='a7N4YGpQ6Dif6IlU8dpWBUY1',
        scope='https://www.googleapis.com/auth/calendar')

    # To disable the local server feature, uncomment the following line:
    # FLAGS.auth_local_webserver = False

    # If the Credentials don't exist or are invalid, run through the native client
    # flow. The Storage object will ensure that if successful the good
    # Credentials will get written back to a file.
    storage = Storage('calendar.dat')
    credentials = storage.get()
    if credentials is None or credentials.invalid == True:
      credentials = run(FLOW, storage)

    # Create an httplib2.Http object to handle our HTTP requests and authorize it
    # with our good Credentials.
    http = httplib2.Http()
    http = credentials.authorize(http)

    # Build a service object for interacting with the API. Visit
    # the Google Developers Console
    # to get a developerKey for your own application.
    service = build(serviceName='calendar', version='v3', http=http,
           developerKey='AIzaSyC0xnkNlkbj9VVUAY9e7oO0xm8hx-me-q4')
    return service
