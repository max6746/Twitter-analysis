import tweepy
import csv

def main():
    #twitter secrets
    consumer_key="CONSUMER_KEY"
    consumer_secret="CONSUMER_SECRET"
    access_token="ACCESS_TOKEN"
    access_token_secret="TOKEN_SECRET"
    
    #Auth and initialize API
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    #Call Tweet
    num_of_tweets = 200
    tweets = api.user_timeline(screen_name='elonmusk', count=num_of_tweets)
    
    #Example
    #print(tweets[1].text, tweets[1].created_at, tweets[1].favorite_count)

    #Create list of dict of tweets
    tweet_list = []
    for tweet in tweets:
        tweet_dict = {'Tweet':tweet.text, 'Date': tweet.created_at.date().strftime("%d-%m-%Y"), 'Time': tweet.created_at.time().strftime("%H:%M:%S"), 'Favourite Count': tweet.favorite_count}
        tweet_list.append(tweet_dict)

    #Write tweets to csv
    with open('tweets.csv', mode='w') as csv_file:
        fieldnames = ['Tweet', 'Date', 'Time', 'Favourite Count']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for tweet in tweet_list:
            writer.writerow({'Tweet': tweet['Tweet'], 'Date': tweet['Date'], 'Time': tweet['Time'], 'Favourite Count': tweet['Favourite Count']})    

if __name__ == "__main__":
    main()