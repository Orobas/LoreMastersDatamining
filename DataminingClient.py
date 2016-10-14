#LoreMastersDatamining
import tweepy
import json
import pymongo
import time
import sys
from pymongo import MongoClient
client = MongoClient()
db = client.TwitterData
consumer_key = 'ctdarrZUCYmhfaLIRMViweNYM'
consumer_secret = 'RZKEPj4XMUY0KKwlw6ARz45RYZ837pB3ucojuFh7kEsHegAuOV'
access_token = '762001840422649856-OYlygYN8Q5CslE1uV6dXW0YVyEoHkaP'
access_token_secret = '5RXedN8QkTIrvHeTpZtTDNtvPWt9qrB4EmS1wDnTNx6ko'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
start = time.time()

def writeToDb(dbnum, result):
	db.altcoin.insert_one({"Date":result["created_at"],"Id":result["id_str"],"Text":result["text"]})
	
class StreamListener(tweepy.StreamListener):

	def on_status(self, status):
		print(status.text)
		
	def on_data(self, data):
		global add
		global minute
		result = json.loads(data)
		id = result["id_str"]
		created = result["created_at"]
		text = result["text"]
		if "altcoin" in text.lower(): db.altcoin.insert_one({"Date":result["created_at"],"Id":result["id_str"],"Text":result["text"]})
		if "bitcoin" in text.lower(): db.bitcoin.insert_one({"Date":result["created_at"],"Id":result["id_str"],"Text":result["text"]})
		if "coindesk" in text.lower(): db.coindesk.insert_one({"Date":result["created_at"],"Id":result["id_str"],"Text":result["text"]})
		if "cryptocurrency" in text.lower(): db.cryptocurrency.insert_one({"Date":result["created_at"],"Id":result["id_str"],"Text":result["text"]})
		if "gold" in text.lower(): db.gold.insert_one({"Date":result["created_at"],"Id":result["id_str"],"Text":result["text"]})
		if "appl" in text.lower(): db.appl.insert_one({"Date":result["created_at"],"Id":result["id_str"],"Text":result["text"]})
		if "goog" in text.lower(): db.goog.insert_one({"Date":result["created_at"],"Id":result["id_str"],"Text":result["text"]})
		if "yhoo" in text.lower(): db.yhoo.insert_one({"Date":result["created_at"],"Id":result["id_str"],"Text":result["text"]})
		curtime = int(time.time()-start)
		if (curtime % 60) == 1: add = True
		if (curtime % 60) == 0 and add: 
			add=False
			minute+=1
			print(minute)


		
twitterStreamListener = StreamListener()
twitterStream = tweepy.Stream(auth = api.auth, listener=StreamListener())
minute = 0
add=True
print "Started program"
twitterStream.filter(track=['altcoin,bitcoin,coindesk,cryptocurrency,gold,APPL,GOOG,YHOO'])
api.update_status('Test tweet for datamining')


