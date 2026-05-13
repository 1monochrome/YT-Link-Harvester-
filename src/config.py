from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_FILE = OUTPUT_DIR / "latest_videos.txt"

MAX_VIDEOS = 5
REQUEST_TIMEOUT = 15
