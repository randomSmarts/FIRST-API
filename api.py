import json
import requests
import pandas as pd

headers = {"Authorization": "Basic cnNteXQ6RjQ1MjdCNUItRTU5Mi00RDdGLTlDODYtMjRERDNEOTYyRTk3"}


def getURL(num):
    return f"https://ftc-api.firstinspires.org/v2.0/2022/teams?teamNumber={num}"

#where it says 10355, just input any team number
result = requests.get(getURL(10355), headers=headers)
bob = result.json()
print(bob["teams"][0]["city"])
#where it says city, you can add other variables or data you want

#https://docs.google.com/spreadsheets/d/1loVY20_LnsC1aNcyqeIiJJ4w5GhtdU52kSwa3viK89w/gviz/tq?tqx=out:csv
# SHEET_ID = '1loVY20_LnsC1aNcyqeIiJJ4w5GhtdU52kSwa3viK89w'
# SHEET_NAME = 'Copy of Loony Squad Open Source Claw participants'
# url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
# df = pd.read_csv(url)
# print(df.head())
