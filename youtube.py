import re
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
import pandas as pd
import datetime
import time

DEVELOPER_KEY = 'API_KEY_HERE' #유튜브 API 키 값
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)
request = youtube.search().list(part="snippet", channelId='')
response = request.execute()
print(response)
