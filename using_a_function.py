"""
This is importing a function named `tweet` from a file
    that we unfortunately don't have access to change.

You use it like so:
>>> tweet("Hello this is my tweet")

If the function cannot connect to Twitter,
    the function will raise a `CommunicationError`
If the message is too long,
    the function will raise a `MessageTooLongError`
"""
from twitter import (
    tweet,
    MessageTooLongError,
    CommunicationError,
)


message = input("What would you like to tweet?  ")
try:
    tweet(message)
except CommunicationError:
    print("An error occured attempting to connect to Twitter. Please try again!")
except MessageTooLongError as e:
    print("Oh No! Your message was too long ({})".format(e))