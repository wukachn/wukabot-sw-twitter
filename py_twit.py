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
BEARER_TOKEN = environ['BEARER_TOKEN']
API_KEY = environ['API_KEY']
API_KEY_SECRET = environ['API_KEY_SECRET']
ACCESS_TOKEN = environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = environ['ACCESS_TOKEN_SECRET']

# Interval between tweets, (60 * 30) = 30 minutes
TWEET_INTERVAL = 60 * 30

# V1 Auth
auth = tweepy.auth.OAuthHandler(API_KEY, API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# V2 Auth
client = tweepy.Client(consumer_key=API_KEY,
                       consumer_secret=API_KEY_SECRET,
                       access_token=ACCESS_TOKEN,
                       access_token_secret=ACCESS_TOKEN_SECRET)

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
    client.create_tweet(text=tweet_text, media_ids=media_ids)

    # Wait specified amount of time, then repeat tweeting process
    time.sleep(TWEET_INTERVAL)
