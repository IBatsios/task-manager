import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

# Google Calendar API scope
SCOPES = ["https://www.googleapis.com/auth/calendar.events"]

def get_credentials():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
            from google.auth.exceptions import GoogleAuthError
            import webbrowser

            try:
                print("🔐 Opening browser for Google sign-in...")
                creds = flow.run_local_server(port=0)
            except KeyboardInterrupt:
                print("\n❌ Cancelled by user (Ctrl+C)")
                sys.exit(1)
            except GoogleAuthError as e:
                print(f"\n❌ Authentication failed: {e}")
                sys.exit(1)
            except Exception as e:
                print(f"\n❌ Unexpected error: {e}")
                sys.exit(1)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return creds
