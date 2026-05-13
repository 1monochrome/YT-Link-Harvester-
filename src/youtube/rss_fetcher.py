import logging
import requests
import feedparser

from src.config import MAX_VIDEOS, REQUEST_TIMEOUT
from src.exceptions import FeedFetchError
from src.youtube.models import Video

logger = logging.getLogger(__name__)


def get_channel_id(handle: str) -> str:
    url = f"https://www.youtube.com/@{handle}"

    response = requests.get(url, timeout=REQUEST_TIMEOUT)

    if response.status_code != 200:
        raise FeedFetchError(
            f"Failed to access channel page. Status: {response.status_code}"
        )

    marker = 'https://www.youtube.com/feeds/videos.xml?channel_id='

    start = response.text.find(marker)

    if start == -1:
        raise FeedFetchError("Channel RSS feed not found.")

    start += len(marker)
    end = response.text.find('"', start)

    return response.text[start:end]



def fetch_latest_videos(channel_id: str):
    rss_url = (
        f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
    )

    logger.info("Fetching RSS feed: %s", rss_url)

    feed = feedparser.parse(rss_url)

    if not feed.entries:
        raise FeedFetchError("No videos found in RSS feed.")

    videos = []

    for entry in feed.entries[:MAX_VIDEOS]:
        videos.append(
            Video(
                title=entry.title,
                video_id=entry.yt_videoid
            )
        )

    return videos
