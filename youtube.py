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

views=[]
likes=[]
title=[]

# request = youtube.search().list(part='snippet', channelId='채널ID')
# request = youtube.videos().list(part='snippet', channelId='채널ID')
request = youtube.playlistItems().list(part="snippet", playlistId='플레이리스트ID')

# https://stackoverflow.com/questions/18953499/youtube-api-to-fetch-all-videos-on-a-channel

# Query execution
response = request.execute()
# Print the results
print(response)

# https://blog.naver.com/leenk1006/222454926151

video_names=[]
video_ids=[]
date=[]

for v in response['items']:
    video_names.append(v['snippet']['title'])
    video_ids.append(v['snippet']['resourceId']['videoId'])
    date.append(v['snippet']['publishedAt'])
    
vdf=pd.DataFrame([date,video_names,video_ids]).T
vdf.columns=['Date','Title','IDS']

category_id=[]
views=[]
likes=[]
dislikes=[]
comments=[]
mins=[]
seconds=[]
title=[]
date=[]

for u in range(len(vdf)):
    request=youtube.videos().list(
    part='snippet,contentDetails,statistics',
    id=vdf['IDS'][u])
    
    response=request.execute()
    
    if response['items']==[]:
        video_ids.append('-')
        category_id.append('-')
        views.append('-')
        likes.append('-')
        dislikes.append('-')
        comments.append('-')
        date.append('-')
        
    else :
        title.append(response['items'][0]['snippet']['title'])
        category_id.append(response['items'][0]['snippet']['categoryId'])
        views.append(response['items'][0]['statistics']['viewCount'])
        likes.append(response['items'][0]['statistics']['likeCount'])
        comments.append(response['items'][0]['statistics']['commentCount'])
        date.append(response['items'][0]['snippet']['publishedAt'])


dtcu_df=pd.DataFrame([title,category_id,views,likes,comments,date]).T
dtcu_df.columns=['title','category_id','views','likes','comments','date']
dtcu_df

