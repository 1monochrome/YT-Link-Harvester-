import logging

from src.config import OUTPUT_DIR, OUTPUT_FILE

logger = logging.getLogger(__name__)


def write_videos(videos):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        for index, video in enumerate(videos, start=1):
            file.write(
                f"{index}. {video.title}\n"
                f"Video ID: {video.video_id}\n\n"
            )

    logger.info("Output written to %s", OUTPUT_FILE)
