import gspread
from oauth2client.service_account import ServiceAccountCredentials

def post(tweet_list):
    #Auth and initialize gcp API
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)

    #open GoogleSheet
    sheet = client.open('elon_tweets').sheet1
    
    #initialize sheet
    sheet.update_cell(1,1, 'SN')
    sheet.update_cell(1,2, 'Tweet')
    sheet.update_cell(1,3, 'Date')
    sheet.update_cell(1,4, 'Time')
    sheet.update_cell(1,5, 'Favourite Count')

    row = 2
    SN = 1
    #Parse Tweet list and write to sheet
    for tweet in tweet_list:
        sheet.update_cell(row, 1, SN)
        sheet.update_cell(row, 2, tweet['Tweet'])
        sheet.update_cell(row, 3, tweet['Date'])
        sheet.update_cell(row, 4, tweet['Time'])
        sheet.update_cell(row, 5, tweet['Favourite Count'])
        row = row+1
        SN = SN+1
