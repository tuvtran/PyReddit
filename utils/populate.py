from app.models.user import User
from app.models.subreddit import Subreddit
from app.models.thread import Link, Text
from app.models.comment import Comment


def generate_data():
    """Generate test data"""
    # creating some subreddits

    subreddits = [
        ('learnprogramming', 'Learn programming'),
        ('anime', 'Place to discuss anime'),
        ('programming', 'Programming in general'),
        ('rust', 'Rust will save the world'),
        ('memes', 'Memes are healthy for students'),
        ('news', 'Stuff going on right now'),
        ('gifs', 'Cat pics')
    ]

    for sub in subreddits:
        Subreddit(name=sub[0], description=sub[1]).save()

    # create a test user
    User(name='admin', email='admin@pyreddit.com', password='test').save()
    User(name='mod1', email='mod1@pyreddit.com', password='test').save()
    User(name='datguy', email='a@pyreddit.com', password='test').save()
    User(name='thechosenone', email='b@pyreddit.com', password='test').save()
    User(name='obama', email='c@pyreddit.com', password='test').save()

    # Create some links
    texts = [
        ('Learn programming for free', 'Hi everyone...', 1, 1),
        ('New anime airing this month', "Here's some anime", 1, 2),
        ('C++ 17 has been released', ' Starting in 2012, the committee has transitioned to a “decoupled” model where major pieces of work can progress independently from the Standard itself and be delivered in “beta feature branch” TSes. Vendors can choose to implement these, and the community can gain experience with the std::experimental version of each feature. This lets us learn and adjust each feature’s design based on experience before it is cast in stone when merged into the “trunk” C++ Standard itself. In the meantime, the Standard can be delivered on a more regular cadence with smaller and more predictable batches of features. This approach also helps C++ compilers to track the Standard more closely and add both the experimental and the draft-final C++ features in a more consistent order. Many TSes are focusing particularly on producing new C++ standard libraries; to participate, see the instructions for how to Submit a Proposal. See the table below for current status.', 1, 3),
        ('Will Rust replace C++?', 'Regarding the latest update from Mozilla', 1, 4),
    ]

    links = [
        ('Programming practices', 'http://exercism.io/', 1, 1),
        ('Anime news', 'https://www.animenewsnetwork.com/', 1, 2),
        ('Hacker News', 'https://news.ycombinator.com/', 1, 3),
        ('Rust', 'https://www.rust-lang.org/en-US/', 1, 4),
        ('How to write an emulator', 'http://emulator101.com/', 1, 3)
    ]

    for t in texts:
        Text(title=t[0], text=t[1], user_id=t[2], subreddit_id=t[3]).save()

    for l in links:
        Link(title=l[0], link=l[1], user_id=l[2], subreddit_id=l[3]).save()

    for i in range(1, 5):
        add_comment_text(i)

    for i in range(1, 6):
        add_comment_link(i)


def add_comment_link(id):

    c1 = Comment(
        content="This link is awesome",
        user_id=1,
        link_id=id
    )
    c1.save()

    c2 = Comment(
        content='This',
        user_id=2,
        comment_id=c1.id
    )
    c2.save()

    c3 = Comment(
        content="Upvote instead of comment 'this' lmao",
        user_id=3,
        comment_id=c2.id
    )
    c3.save()

    c4 = Comment(
        content="I read the same thing last night too",
        user_id=4,
        link_id=id
    )
    c4.save()

    c5 = Comment(
        content="Really?????",
        user_id=1,
        comment_id=c4.id
    )
    c5.save()


def add_comment_text(id):

    c1 = Comment(
        content="This text is awesome",
        user_id=1,
        text_id=id
    )
    c1.save()

    c2 = Comment(
        content='This',
        user_id=2,
        comment_id=c1.id
    )
    c2.save()

    c3 = Comment(
        content="Upvote instead of comment 'this' lmao",
        user_id=3,
        comment_id=c2.id
    )
    c3.save()

    c4 = Comment(
        content="I read the same thing last night too",
        user_id=4,
        text_id=id
    )
    c4.save()

    c5 = Comment(
        content="Really?????",
        user_id=1,
        comment_id=c4.id
    )
    c5.save()
