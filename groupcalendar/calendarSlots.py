from apiclient.discovery import build
from oauth2client.client import OAuth2WebServerFlow
from auth import create_service

#import httplib2

#Params: user email as string
#Returns: A list of Event objects from the Calendar
#Given a calendar, gets a list of events
def events_get(service,email):
    events = service.events().list(calendarId='primary', pageToken=page_token).execute()
    return events

#Params: service, list of emails as strings
#Returns: A list of Event objects from all Calendars
#Returns a list of all events across the emails
def compile_total_events(service, emails):
    event_list = []
    for email in emails:
        event_list += events_get(service,email)
    return event_list

#Params: list of emails as strings
#Returns: Calendar object
#Takes events from all emails and puts them together in 1 calendar
def merge_calendars(emails):
    calendar_info = {
        'summary':'Merged calendar',
        'timeZone':'America/Los_Angeles' #find the best timezone across calendars
    }
    calendar_service = create_service()
    merged_calendar = calendar_service.calendars().insert(body=calendar_info).execute()
    all_events = compile_total_events(calendar_service,emails)
    for event in all_events:
        calendar_service.events().insert(calendarId=merged_calendar['id'],body=event).execute()
    return merged_calendar #Return the list of events instead from above?    
