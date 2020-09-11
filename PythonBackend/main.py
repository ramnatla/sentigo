import os
import tweepy as tw
import json
from imageAnalyzer import score_detected_faces
import urllib.request as req
import statistics as stats
from sentimentAnalyzer import get_sentiment


def run(keyword, num_posts = 50):
	twitter_consumer_key = os.environ.get("TWITTER_CONSUMER_KEY")
	twitter_consumer_secret = os.environ.get("TWITTER_CONSUMER_SECRET")
	twitter_access_token_key = os.environ.get("TWITTER_ACCESS_TOKEN_KEY")
	twitter_access_token_secret = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")
	
	auth = tw.OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
	auth.set_access_token(twitter_access_token_key, twitter_access_token_secret)
	twitterApi = tw.API(auth, wait_on_rate_limit=True)

	# Query Twitter with input keywords
	tweets = tw.Cursor(twitterApi.search,
				q=keyword,
				lang="en",).items(num_posts)

	iter = 0
	imgurls = []
	# Iterate and print tweets
	tweetToVal = dict()
	for tweet in tweets:
		js = tweet._json
		text = tweet.text
		sent = get_sentiment(text)
		if(sent > -2):
			tweetToVal[text] = sent
		else:
			continue
		
		# Attached images to tweets
		if "extended_entities" in js:
			for i in js["extended_entities"]["media"]:
				imgurl = i["media_url_https"]
				req.urlretrieve(imgurl, "image_name.jpg")
				temp = score_detected_faces("./image_name.jpg")
				if(temp > -2):
					imgurls.append(imgurl)
					sent = tweetToVal[list(tweetToVal.keys())[-1]]
					sent = (temp + sent)/2
					tweetToVal[list(tweetToVal.keys())[-1]] = sent

		iter += 1

	if(len(tweetToVal.keys()) > 0):
		avg = stats.mean(list(tweetToVal.values()))
	else:
		avg = "no data"

	# Get most positive and negative posts
	best = []
	worst = []
	vals = list(tweetToVal.values())
	tweets = list(tweetToVal.keys())
	for i in range(5):
		if(len(vals) > 0):
			if(max(vals) > 0.1):
				bestLocation = vals.index(max(vals))
				best.append(tweets[bestLocation])
				del vals[bestLocation]
				del tweets[bestLocation]

		if(len(vals) > 0):
			if(min(vals) < -0.1):
				worstLocation = vals.index(min(vals))
				worst.append(tweets[worstLocation])
				del vals[worstLocation]
				del tweets[worstLocation]


	all = dict()
	all['sentiment'] = avg
	all['postsAnalyzed'] = num_posts
	all['imagesAnalyzed'] = len(imgurls)
	all['positivePosts'] = best
	all['negativePosts'] = worst
	all['urls'] = imgurls
	return all
