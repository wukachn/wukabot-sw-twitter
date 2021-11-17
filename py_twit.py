from os import environ
import glob
import random
import tweepy
import time


# Gets two random .png files from the folder given as a parameter.
def RandomSWChars(folder):
        file_path_type = [folder + "*.png"]
        images = glob.glob(random.choice(file_path_type))
        return [random.choice(images), random.choice(images)]

# Establishes credentials for twitter api access
# Defined through heroku
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

# Interval between tweets, (60 * 30) = 30 minutes
TWEET_INTERVAL = 60 * 30

# Authorise twitter API connection
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# Tweet a battle, scheduled with TWEET_INTERVAL
while True:
    # Add character images to the tweet
    sw_chars = RandomSWChars("sw_char/")
    while (sw_chars[0]==sw_chars[1]):
        sw_chars = RandomSWChars("sw_char/")
        
    media_ids = [api.media_upload(i).media_id_string for i in sw_chars]

    # Extract character names from .png file names.
    for i in range(len(sw_chars)):
        sw_chars[i] = sw_chars[i].replace('sw_char/', '').replace('.png', '')

    # Post tweet
    tweet_text = "STAR WARS DEATH BATTLE!\n" + sw_chars[0] + " VS " + sw_chars[1]
    api.update_status(status=tweet_text, media_ids=media_ids)

    # Wait specified amount of time, then repeat tweeting process
    time.sleep(TWEET_INTERVAL)
