from os.path import isfile
import praw
import pandas as pd
from time import sleep
from praw_info import reddit_info

# Get credentials from instance in praw_info.py
reddit = praw.Reddit(client_id = reddit_info['client_id'],
                        client_secret = reddit_info['client_secret'],
                        user_agent = reddit_info['user_agent'],
                        username = reddit_info['username'],
                        password = reddit_info['password'])

foodporn = reddit.subreddit('foodporn')

post_list = []
for post in foodporn.top('all', limit = 10000):
    post_list.append(post.title)

print(post_list)

df = pd.DataFrame(post_list)
df.to_pickle('data/posts.pkl')