import requests
import datetime
from time import sleep
from typing import List

from search.models import Videos
from youtube_api.settings import API_KEYS, YOUTUBE_HOST, MAX_DEPTH


KEYS = API_KEYS.split(',') # API_KEY set as comma separated values string
KEY_INDEX = 0 # Index pointing to the key number in keys available


def save_videos(video_list: List[dict]):
    for video_data in video_list:
        # Using update or create here so that same video doesn't gets saved anyhow
        Videos.objects.update_or_create(
            id=video_data['id']['videoId'],
            defaults={
                'title': video_data['snippet']['title'],
                'description': video_data['snippet']['description'],
                'published_at': video_data['snippet']['publishedAt'],
                'thumbnails': video_data['snippet']['thumbnails']
            }
        )
        

def get_paged_result(publishedDate: datetime.datetime) -> List[dict]:
    video_list = []
    global KEY_INDEX
    payload = {
        'q': 'music',
        'type': 'video',
        'order': 'date',
        'part': 'snippet',
        'publishedAfter': datetime.datetime.strftime(publishedDate, '%Y-%m-%dT%H:%M:%SZ'),
        'key': KEYS[KEY_INDEX],
        'maxResults': 50
    }
    # Initial request
    response = requests.get(
        url=f'{YOUTUBE_HOST}/search',
        params=payload
    )

    if response.ok and response.json().get('items'):
        video_list.extend(response.json().get('items'))
        payload['pageToken'] = response.json().get('nextPageToken')
        i = 1
        # Make continuous calls to youtube api to get the results until maximum depth is reached.
        while i < min(MAX_DEPTH, response.json()['pageInfo']['totalResults']) and payload['pageToken']:
            response = requests.get(
                url=f'{YOUTUBE_HOST}/search',
                params=payload
            )
            if response.ok and response.json().get('items'):
                video_list.extend(response.json().get('items'))
                payload['pageToken'] = response.json().get('nextPageToken')
                i = i + 1
            elif response.status_code == 403 and response.json()['error']['errors'][0]['reason'] == 'quotaExceeded':
                KEY_INDEX = KEY_INDEX + 1 if KEY_INDEX < (len(KEYS)-1) else 0

    elif response.status_code == 403 and response.json()['error']['errors'][0]['reason'] == 'quotaExceeded':
        KEY_INDEX = KEY_INDEX + 1 if KEY_INDEX < (len(KEYS)-1) else 0
    
    return video_list


def poll_youtube():
    # Initial sleep
    sleep(5)

    # Query db to check until when the videos are stored in the DB.
    video = Videos.objects.order_by('-published_at').first()
    publishedDate = datetime.datetime.now().replace(hour=0, minute=0, second=0) if video is None else video.published_at
    while True:
        print(f'Attempting to fetch after {publishedDate}')

        # Fetch the List of youtube videos result
        videos = get_paged_result(
            publishedDate=publishedDate
        )

        # if list is not empty, save the values
        if videos:
            print(f'Attempting to save {len(videos)} after {publishedDate}')
            save_videos(videos)

            # Increasing published at to now
            publishedDate = datetime.datetime.now()
        sleep(15)
