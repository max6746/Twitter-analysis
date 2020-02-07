import pandas
import csv
import datetime

def get_stock(date, stock_file):
    stock_df = pandas.read_csv(stock_file)
    for ind in stock_df.index:
        if stock_df['Date'][ind]:
            #try previous stock
            try:
                pre = stock_df['Date'][ind-1]
            except:
                pre = 'null'
            #try with curr date
            curr = stock_df['Date'][ind]
            #try next stock
            try:
                post = stock_df['Date'][ind+1]
            except:
                post = 'null'
        else:
            date_obj = datetime.datetime.strptime(date, "%d-%m-%Y").date()
            cmp_date = datetime.datetime.strptime(stock_df['Date'][ind], "%d-%m-%Y").date()
            if date_obj < cmp_date:
                try:
                    pre = stock_df['Date'][ind-1]
                except:
                    pre = 'null'
                #try with curr date
                curr = 'null'
                post = stock_df['Date'][ind]
    return({"pre":pre, "curr": curr, "post": post})    

def write_to_csv(date, tweet_list, fav_list, time_list, stock_file):
    stock_dict = get_stock(date, stock_file)
    # with open('tweets.csv', mode='w') as csv_file:
    #     fieldnames = ['Tweet', 'Date', 'Time', 'Favourite Count']
    #     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    #     writer.writeheader()
    #     for tweet in tweet_list:
    #         writer.writerow({'Tweet': tweet['Tweet'], 'Date': tweet['Date'], 'Time': tweet['Time'], 'Favourite Count': tweet['Favourite Count']})    


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
        write_to_csv(date, tweet_list, fav_list, time_list, stock_file)

