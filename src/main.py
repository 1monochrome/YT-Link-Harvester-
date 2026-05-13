import logging
import os
import sys

from src.logger import setup_logger
from src.youtube.channel_parser import extract_handle
from src.youtube.rss_fetcher import get_channel_id, fetch_latest_videos
from src.services.txt_writer import write_videos
from src.exceptions import YoutubeFetcherError

setup_logger()

logger = logging.getLogger(__name__)


def main():
    try:
        channel_url = os.getenv("CHANNEL_URL")

        if not channel_url:
            raise ValueError("CHANNEL_URL environment variable is missing.")

        logger.info("Processing channel: %s", channel_url)

        handle = extract_handle(channel_url)
        logger.info("Extracted handle: %s", handle)

        channel_id = get_channel_id(handle)
        logger.info("Resolved channel ID: %s", channel_id)

        videos = fetch_latest_videos(channel_id)
        logger.info("Fetched %d videos", len(videos))

        write_videos(videos)

        logger.info("Process completed successfully.")

    except YoutubeFetcherError as error:
        logger.exception("Application error: %s", error)
        sys.exit(1)

    except Exception as error:
        logger.exception("Unexpected error: %s", error)
        sys.exit(1)


if __name__ == "__main__":
    main()
