from google.oauth2.credentials import Credentials
import gspread
from googleapiclient.discovery import build

# use creds to create a client to interact with the Google Drive API
creds = Credentials.from_authorized_user_info(info={"client_id": "326734701468-kaqa6697u4ehc49edqtkhjrfu06d9o7c.apps.googleusercontent.com",
                                                      "client_secret": "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",
                                                      "refresh_token": "YOUR_REFRESH_TOKEN"})
service = build('drive', 'v3', credentials=creds)

# Find a workbook by url
spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1loVY20_LnsC1aNcyqeIiJJ4w5GhtdU52kSwa3viK89w/edit#gid=0'
file_id = spreadsheet_url.split('/')[-2]
sheet_metadata = service.files().get(fileId=file_id, fields='sheets.properties').execute()
sheets = sheet_metadata.get('sheets', '')
sheet_map = {}
for sheet in sheets:
    title = sheet.get("properties", {}).get("title", "Sheet1")
    sheet_id = sheet.get("properties", {}).get("sheetId", 0)
    sheet_map[title] = sheet_id

# Extract all the data from column 2
sheet = service.spreadsheets().values().get(spreadsheetId=file_id, range='Sheet1!B:B').execute()
column_2_data = sheet.get('values', [])

# Print the data
print(column_2_data)
