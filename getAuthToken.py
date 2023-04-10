import msal # pip install msal
import json
import requests # pip install requests


def get_access_token():
    tenantID = '' #replace with yours
    authority = 'https://login.microsoftonline.com/' + tenantID
    clientID = '' # replace with yours
    clientSecret = '' # replace with yours
    scope = ['https://graph.microsoft.com/.default']
    app = msal.ConfidentialClientApplication(clientID, authority=authority, client_credential = clientSecret)
    access_token = app.acquire_token_for_client(scopes=scope)
    return access_token

# token block
access_token = get_access_token()
token = access_token['access_token']

print(token)
