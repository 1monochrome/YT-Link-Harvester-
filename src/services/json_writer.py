import os
import json
import logging
from dataclasses import asdict

from src.config import OUTPUT_DIR
from src.exceptions import OutputWriteError

logger = logging.getLogger(__name__)


def write_videos_json(videos, filename="latest_videos.json"):
    try:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        path = os.path.join(OUTPUT_DIR, filename)

        payload = [asdict(v) for v in videos]

        with open(path, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)

        return path

    except Exception as exc:
        logger.exception("Failed to write JSON output")
        raise OutputWriteError(str(exc)) from exc
