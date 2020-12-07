import time
import math
import praw

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
    reddit = init_reddit()
    count = 0
    while True:
        count += 1
        print(f'[{math.trunc(time.time())}]: Working v3', count, display_karma(reddit))
        time.sleep(5)

if __name__ == "__main__":
    main()
