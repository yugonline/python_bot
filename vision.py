'''
=================================================================
Commands Required:

cd google-cloud-sdk/
cd bin/
gcloud init

Please set GOOGLE_APPLICATION_CREDENTIALS or
explicitly create credential and re-run the application. For more
information, please see
https://developers.google.com/accounts/docs/application-default-credentials.

gcloud beta auth application-default login
=================================================================
'''

import io
from google.cloud import vision
client = vision.Client()
# client = datastore.Client()
# client = vision.Client(project='LinkGrabber', credentials=cred)s	
