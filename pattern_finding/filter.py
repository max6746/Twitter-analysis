import pandas
import csv

# def get_stock(date, stock):
#     stock_df = pandas.read_csv(stock)
#     for date in df
#     for ind in stock_df.index:
#         try:
#             pre = stock

# def write_to_csv(date, tweet_list, fav_list, time_list):
#     with open('tweets.csv', mode='w') as csv_file:
#         fieldnames = ['Tweet', 'Date', 'Time', 'Favourite Count']
#         writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#         writer.writeheader()
#         for tweet in tweet_list:
#             writer.writerow({'Tweet': tweet['Tweet'], 'Date': tweet['Date'], 'Time': tweet['Time'], 'Favourite Count': tweet['Favourite Count']})    


def cleanup(tweet, stock):
    df = pandas.read_csv(tweet)

    #sort tweets by date
    unique_dates = list(set(df['Date']))

    #sort dates
    unique_dates.sort()

    for date in unique_dates:
        tweet_list = []
        fav_list = []
        time_list = []
        for index,row in df.iterrows():
            if date == row['Date']:
                tweet_list.append(row['Tweet'])
                fav_list.append(row['Favourite Count'])
                time_list.append(row['Time'])
        write_to_csv(date, tweet_list, fav_list, time_list)

