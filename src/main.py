import os

from src.logger import setup_logger
from src.youtube.rss_fetcher import extract_handle, get_channel_id, fetch_latest_videos
from src.services.txt_writer import write_videos_txt
from src.services.json_writer import write_videos_json

def main():
    setup_logger()

    channel_url = os.getenv("CHANNEL_URL", "").strip()

    if not channel_url:
        raise ValueError("CHANNEL_URL is required")

    handle = extract_handle(channel_url)
    channel_id = get_channel_id(handle)
    videos = fetch_latest_videos(channel_id)

    txt_path = write_videos_txt(videos)
    json_path = write_videos_json(videos)

    print(f"TXT saved to: {txt_path}")
    print(f"JSON saved to: {json_path}")


if __name__ == "__main__":
    main()
