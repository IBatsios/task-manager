import pandas as pd
from googleapiclient.discovery import build
from google_auth import get_credentials
from datetime import datetime, timedelta

def add_event_to_calendar(task, company, deadline, reminder=False):
    creds = get_credentials()
    service = build("calendar", "v3", credentials=creds)

    deadline_dt = pd.to_datetime(deadline)
    end_time = deadline_dt + timedelta(minutes=30)

    event = {
        "summary": f"{task} [{company}]",
        "description": f"Task from CLI",
        "start": {
            "dateTime": deadline_dt.isoformat(),
            "timeZone": "America/New_York"  # change as needed
        },
        "end": {
            "dateTime": end_time.isoformat(),
            "timeZone": "America/New_York"
        },
    }

    if reminder:
        event["reminders"] = {
            "useDefault": False,
            "overrides": [
                {"method": "popup", "minutes": 10}
            ]
        }

    service.events().insert(calendarId="primary", body=event).execute()
    print("✅ Event added to Google Calendar")
