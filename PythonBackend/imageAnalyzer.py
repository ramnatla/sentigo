# Imports the Google Cloud vision client library
from google.cloud import vision
import io
import statistics as stats

client = vision.ImageAnnotatorClient()

# Calculates a score for the expressions on faces detected in images
def score_detected_faces(path):
	with io.open(path, 'rb') as image_file:
	    content = image_file.read()

	image = vision.types.Image(content=content)

	response = client.face_detection(image=image)
	faces = response.face_annotations

	# Names of likelihood from google.cloud.vision.enums
	likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
	                    'LIKELY', 'VERY_LIKELY')

	likelihood_names = ['UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
	                    'LIKELY', 'VERY_LIKELY']

	values = []
	for face in faces:
	    # print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
	    # print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
	    # print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))
	    if likelihood_names.index(likelihood_name[face.anger_likelihood]) == 0:
	    	angerSent = 0
	    else:
	    	angerSent = -0.25 * (likelihood_names.index(likelihood_name[face.anger_likelihood])-1)

	    if likelihood_names.index(likelihood_name[face.joy_likelihood]) == 0:
	    	joySent = 0
	    else:
	    	joySent = 0.25 * (likelihood_names.index(likelihood_name[face.joy_likelihood])-1)

	    values.append(joySent + angerSent)

	if((len(values) == 1 and values[0] == 0) or len(values) == 0):
		return float("-inf")
	else:
		return stats.mean(values)