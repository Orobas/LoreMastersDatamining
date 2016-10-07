#LoreMastersDatamining
import tweepy
consumer_key = 'ctdarrZUCYmhfaLIRMViweNYM'
consumer_secret = 'RZKEPj4XMUY0KKwlw6ARz45RYZ837pB3ucojuFh7kEsHegAuOV'
access_token = '762001840422649856-OYlygYN8Q5CslE1uV6dXW0YVyEoHkaP'
access_token_secret = '5RXedN8QkTIrvHeTpZtTDNtvPWt9qrB4EmS1wDnTNx6ko'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

class StreamListener(tweepy.StreamListener):

	def on_status(self, status):
		print(status.text)
		
	def on_data(self, data):
		print(data)

		
twitterStreamListener = StreamListener()
twitterStream = tweepy.Stream(auth = api.auth, listener=StreamListener())

twitterStream.filter(track=['gold'])
api.update_status('Test tweet for datamining')


