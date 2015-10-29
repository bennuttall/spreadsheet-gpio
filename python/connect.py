import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials
from time import sleep

json_key = json.load(open('gdrive.json'))
scope = ['https://spreadsheets.google.com/feeds']
email = json_key['client_email']
private_key = json_key['private_key'].encode()
credentials = SignedJwtAssertionCredentials(email, private_key, scope)
gc = gspread.authorize(credentials)

def open_worksheet(name):
    return gc.open(name).sheet1

def read_cell(wks, r, c):
    return wks.cell(r, c).numeric_value

def read_cell_continuous(wks, r, c):
    while True:
        yield read_cell(wks, r, c)
        sleep(0.1)
