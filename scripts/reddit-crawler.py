import praw


reddit = praw.Reddit(
    client_id="MikQJvv_RkwBSQ",
    client_secret=None,
    user_agent="macOS:PyReddit:0.0.1 by /u/hacknrk")

print(reddit.read_only)


subreddit_list = [
    'programming',
    'cscareerquestions',
    'anime'
]

for sub_name in subreddit_list:
    print('*' * 20)
    subreddit = reddit.subreddit(sub_name)
    print(subreddit.title)

    for submission in subreddit.hot(limit=15):
        print(submission.title)
        print(submission.url)
        print(submission.id)
        print(submission.score)
        print()
