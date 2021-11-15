from os import environ
import glob, random, tweepy, time

def RandomSWChars(folder):
        file_path_type = [folder + "*.png"]
        images = glob.glob(random.choice(file_path_type))
        return [random.choice(images), random.choice(images)]

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

TWEET_INTERVAL = 60 * 30 # tweet every 30 mins

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while True:
	sw_chars = RandomSWChars("sw_char/")
	media_ids = [api.media_upload(i).media_id_string for i in sw_chars]

	for i in range(len(sw_chars)):
	    sw_chars[i] = sw_chars[i].replace('sw_char/', '').replace('.png', '')

	tweet_text = "STAR WARS DEATH BATTLE!\n" + sw_chars[0] + " VS " + sw_chars[1]

	api.update_status(status=tweet_text, media_ids=media_ids)

	time.sleep(600)