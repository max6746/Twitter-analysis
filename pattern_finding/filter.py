import pandas
import csv
import datetime

def get_stock(date, stock_file):
    stock_df = pandas.read_csv(stock_file)
    stock_dic = stock_df.set_index('Date')['Close'].to_dict()
    for ind in stock_df.index:
        if stock_df['Date'][ind]:
            #try previous stock
            try:
                pre_date = stock_df['Date'][ind-1]
                pre_stock = stock_dic[pre_date]
            except:
                pre_date = 'null'
                pre_stock = 'null'
            #try with curr date
            curr_date = stock_df['Date'][ind]
            curr_stock = stock_dic[curr_date]
            #try next stock
            try:
                post_date = stock_df['Date'][ind+1]
                post_stock = stock_dic[post_date]
            except:
                post_date = 'null'
                post_stock = 'null'
        else:
            date_obj = datetime.datetime.strptime(date, "%d-%m-%Y").date()
            cmp_date = datetime.datetime.strptime(stock_df['Date'][ind], "%d-%m-%Y").date()
            if date_obj < cmp_date:
                try:
                    pre_date = stock_df['Date'][ind-1]
                    pre_stock = stock_dic[pre_date]
                except:
                    pre_date = 'null'
                    pre_stock = 'null'
                #try with curr date
                curr_date = 'null'
                curr_stock = 'null'
                
                post_date = stock_df['Date'][ind]
                post_stock = stock_dic[post_date]
    return({pre_date:pre_stock, curr_date: curr_stock, post_date: post_stock})    

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

