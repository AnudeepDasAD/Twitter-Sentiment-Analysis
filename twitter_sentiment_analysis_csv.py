#Name: Anudeep Das
#Date: 16/06/2019
#Purpose: This program asks the user what topic they would like
#            to find the Twitter sentiment about, and then
#            finds the average polarity and subjectivity of that topic.
#            It then stores all of the tweet information in a CSV file.

#String -> String

import csv
import tweepy
from textblob import TextBlob


#Tokenize all of the words

#Find the number of times each word comes up
#  and look at the sentiment value of the words using a lexicon
#  (which has positive and negative sentiments)

#Then classify the total sentiment value of the tweet


#-------------------------Authentication------------------------------
consumer_key = '8wZSca0v9CbsZ6yZxmBLfE8gj'
consumer_secret = 'amkOwzWNQBqGq2H95IlKjH6mISIZ4d2avDLfy4mdiZjDus9aRl'

access_token = '1113108009180205059-rZhdP4PwHF9jCwAJnjajRwQnyUyZvE'
access_token_secret = 'SBfWHzIUyNUhSW4dnmihFNrZKQn2FhMLOHrd2GReKGgoP'


#Must authenticate with Twitter (login via code)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#--------------------------------ANALYSIS------------------------------

#creating the csv file

#'w' is for 'write'

'''with open('csv_file_1.csv', 'w', newline='') as f:
    thewriter = csv.writer(f)
    thewriter.writerow(['col1', 'col2'])'''

number_of_tweets = 0
total_polarity = 0
total_subj = 0


#api variable created, can do stuff with tweets now
api = tweepy.API(auth)

#Must store list of tweets (search)
#public_tweets = api.search('Critical Role')

search_topic = input("What would you like to search about?")
public_tweets = api.search(search_topic)

with open('csv_file_1.csv', 'w', newline='') as f:
    thewriter = csv.writer(f)

    #Use a for-loop to go through all of the tweets 
    for tweet in public_tweets:
        #Prints the actual tweet
        #print(tweet.text)

        #create the analysis variable
        analysis = TextBlob(tweet.text)
        print(analysis.sentiment)
        thewriter.writerow([analysis.sentiment])

        number_of_tweets += 1
        total_polarity += analysis.sentiment.polarity
        total_subj += analysis.sentiment.subjectivity

    #polarity is how positive/negative it is and subjectivity is
    #  the degree of how factual it is


    if number_of_tweets <=0:
        print("There were no tweets about that topic")
        thewriter.writerow(['There were no tweets about that topic'])
    else:
        print("AVERAGE POLARITY: {}".format(total_polarity/number_of_tweets))
        print("AVERAGE SUBJECTIVITY: {}".format(total_subj/number_of_tweets))

        thewriter.writerow(["AVERAGE POLARITY: {}".format(total_polarity/number_of_tweets)])
        thewriter.writerow(["AVERAGE SUBJECTIVITY: {}".format(total_subj/number_of_tweets)])

    avg_pol = total_polarity/number_of_tweets
    avg_subj = total_subj/number_of_tweets

    summary_pol = ''
    summary_subj = ''

    if avg_pol < 0:
        summary_pol = ("Most of the tweets were negative")
    elif avg_pol > 0:
        summary_pol = ("Most of the tweets were positive")
    else:
        summary_pol = ("People are indifferent about this topic: {}".format(search_topic))

    if avg_subj > 0.5:
        summary_subj = ("Most of the tweets were subjective")
    elif avg_subj < 0.5:
        summary_subj = ("Most of the tweets were factual")
    else:
        summary_subj = ("There were aprroximately equal amounts of factuality and opinion")

    thewriter.writerow([summary_pol])
    thewriter.writerow([summary_subj])
