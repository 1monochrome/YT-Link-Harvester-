import logging
import os
import sys

from src.logger import setup_logger
from src.downloader import get_direct_download_link
from src.services.txt_writer import write_videos
from src.services.json_writer import write_json
from src.exceptions import YoutubeHarvesterError
from src.config import TXT_OUTPUT_FILE, JSON_OUTPUT_FILE

setup_logger()
logger = logging.getLogger(__name__)


def main():
    try:
        target_url = os.getenv("TARGET_URL")

        if not target_url:
            raise ValueError("TARGET_URL environment variable is missing.")

        logger.info("Processing URL: %s", target_url)

        data = get_direct_download_link(target_url)

        from src.models import Video
        video = Video(
            title=data["title"],
            video_id=data["video_id"],
            webpage_url=data["webpage_url"],
            direct_url=data["direct_url"],
            duration=data["duration"],
            uploader=data["uploader"],
        )

        videos = [video]

        write_json(videos, JSON_OUTPUT_FILE)
        write_videos(videos, TXT_OUTPUT_FILE)

        logger.info("Done.")
        logger.info("Direct URL: %s", data["direct_url"])

    except YoutubeHarvesterError as error:
        logger.exception("Application error: %s", error)
        sys.exit(1)
    except Exception as error:
        logger.exception("Unexpected error: %s", error)
        sys.exit(1)


if __name__ == "__main__":
    main()
