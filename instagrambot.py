from instapy import InstaPy
from instapy import smart_run

session = InstaPy(username = "usernamehere", password = "passwordhere")
session.login()

session.set_relationship_bounds(enabled = True, max_followers = 200)

session.set_do_follow(True, percentage = 100)
session.like_by_tags(["lifting", "gymmotivation","pr","workout"], amount = 3)

session.end()
