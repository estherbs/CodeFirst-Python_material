# -*- coding: utf-8 -*-
# basic script to send an email
# add attachment

import requests

# loading the info
from keys import *


# email particulars
recipient = 'Esther Barlow-Smith <esther_bs@hotmail.co.uk>'
sender = 'Esther Barlow-Smith <ebarlow-smith1@sheffield.ac.uk>'

subject = 'Hello there-with attachments'

at_file = "Alice.txt"
body_t = "Sending text and attachment!"

# formattting and sending message
request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)
request = requests.post(request_url, auth=('api', key),
    files=[("attachment", open(at_file, ))],
    data={
    'from': sender,
    'to': recipient,
    'subject': subject,
    'text': body_t,
    'html': """<html>HTML version of the body</html>"""})

# checking the status
print ('Status: {0}'.format(request.status_code))
print ('Body:   {0}'.format(request.text))
