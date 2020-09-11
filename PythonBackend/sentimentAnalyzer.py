# Imports the Google Cloud language client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Calculates the sentiment score for a given tweet's text using the Google Natural Language API
def get_sentiment(text):
	# Instantiates a client
	client = language.LanguageServiceClient()
	try:
		document = types.Document(
			content=text,
            type=enums.Document.Type.PLAIN_TEXT)

        # Detects the sentiment of the text
		sentiment = client.analyze_sentiment(document=document).document_sentiment
		if(sentiment.score == 0):
			return float("-inf")
		else:
			return sentiment.score
	except:
		return 0