import os
from instagrapi import Client
from dotenv import load_dotenv, dotenv_values

# Load details from .env file
load_dotenv()

# Login credentials
username = "INSTAGRAM_USERNAME"
password = "INSTAGRAM_PASSWORD"

# Initialize the client
cl = Client()
cl.login(username, password)

# The ID of the post where we want to check for comments
media_id = cl.media_pk_from_url('VIDEO_URL')

# The keyword to look for
keyword = "YOUR_WORD"
# The message to send
message = "YOUR_MESSAGE"

# Fetch all comments
comments = cl.media_comments(media_id)

for comment in comments:
    if keyword.lower() in comment.text.lower():
        user_id = comment.user.pk
        # Send the message to the user's DM
        cl.direct_send(message, [user_id])

# Logout
cl.logout()
