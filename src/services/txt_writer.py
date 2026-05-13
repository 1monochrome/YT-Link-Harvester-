import os
import logging
from src.config import OUTPUT_DIR
from src.exceptions import OutputWriteError

logger = logging.getLogger(__name__)


def write_videos_txt(videos, filename="latest_videos.txt"):
    try:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        path = os.path.join(OUTPUT_DIR, filename)

        with open(path, "w", encoding="utf-8") as f:
            for i, video in enumerate(videos, start=1):
                f.write(f"{i}. {video.title}\n")
                f.write(f"   Video ID: {video.video_id}\n")
                f.write(f"   URL: {video.url}\n\n")

        return path

    except Exception as exc:
        logger.exception("Failed to write TXT output")
        raise OutputWriteError(str(exc)) from exc
