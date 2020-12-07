import os
import time
import math
import praw

product_stuff = ['stuff1', 'stuff2', 'stuff3']
staging_stuff = ['cool stuff', 'buggy stuff']
app_stuff = []

def process_app_level():
    level = os.environ.get('app_level')
    global app_stuff
    if level == 'production':
        app_stuff = product_stuff
    elif level == 'staging':
        app_stuff = staging_stuff
    else:
        app_stuff = staging_stuff

def init_reddit() -> praw.Reddit:
    reddit = praw.Reddit(
        user_agent="srztestbot (by u/srztestbot)",
        client_id="LavqLWzDjVbL9A",
        client_secret="_2Mqo3u4gJf6G2pKrsi1YgaNnwlR6A",
        username="srztestbot",
        password="0tskulti9"
    )

    return reddit

def display_karma(reddit):
    user = reddit.user.me()
    print(f'Karma for {user.name}:', user.comment_karma)

def main():
    print("Starting up")
    process_app_level()
    print(app_stuff)
    reddit = init_reddit()
    count = 0
    while True:
        count += 1
        print(f'[{math.trunc(time.time())}]: Working v3', count, display_karma(reddit))
        time.sleep(5)

if __name__ == "__main__":
    main()
