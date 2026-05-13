import logging
from typing import List, Dict, Any

from yt_dlp import YoutubeDL

from src.config import (
    DEFAULT_USER_AGENT,
    REQUEST_TIMEOUT,
    RETRIES,
    SOURCE_ADDRESS,
    MAX_VIDEOS,
)
from src.exceptions import DownloadError
from src.models import Video

logger = logging.getLogger(__name__)


def _ydl_opts():
    return {
        "quiet": True,
        "skip_download": True,
        "extract_flat": False,
        "socket_timeout": REQUEST_TIMEOUT,
        "retries": RETRIES,
        "source_address": SOURCE_ADDRESS,
        "http_headers": {
            "User-Agent": DEFAULT_USER_AGENT,
            "Accept-Language": "en-US,en;q=0.9",
        },
    }


def extract_video_info(url: str) -> Dict[str, Any]:
    try:
        with YoutubeDL(_ydl_opts()) as ydl:
            info = ydl.extract_info(url, download=False)
            return info
    except Exception as exc:
        logger.exception("Failed to extract video info")
        raise DownloadError(str(exc)) from exc


def get_direct_download_link(url: str) -> Dict[str, Any]:
    info = extract_video_info(url)

    formats = info.get("formats", [])
    valid_formats = [f for f in formats if f.get("url")]

    if not valid_formats:
        raise DownloadError("No downloadable formats found.")

    best = max(valid_formats, key=lambda x: (x.get("height") or 0, x.get("tbr") or 0))

    return {
        "title": info.get("title"),
        "video_id": info.get("id"),
        "webpage_url": info.get("webpage_url") or url,
        "direct_url": best.get("url"),
        "duration": info.get("duration"),
        "uploader": info.get("uploader"),
        "format_id": best.get("format_id"),
        "ext": best.get("ext"),
        "resolution": f"{best.get('height', 'unknown')}p",
    }


def get_latest_videos(url: str, limit: int = MAX_VIDEOS) -> List[Video]:
    info = extract_video_info(url)

    entries = info.get("entries", [])
    if not entries:
        single = get_direct_download_link(url)
        return [
            Video(
                title=single["title"],
                video_id=single["video_id"],
                webpage_url=single["webpage_url"],
                direct_url=single["direct_url"],
                duration=single["duration"],
                uploader=single["uploader"],
            )
        ]

    videos = []
    for entry in entries[:limit]:
        if not entry:
            continue

        direct_url = None
        formats = entry.get("formats", [])
        valid_formats = [f for f in formats if f.get("url")]
        if valid_formats:
            best = max(valid_formats, key=lambda x: (x.get("height") or 0, x.get("tbr") or 0))
            direct_url = best.get("url")

        videos.append(
            Video(
                title=entry.get("title", ""),
                video_id=entry.get("id", ""),
                webpage_url=entry.get("webpage_url", ""),
                direct_url=direct_url,
                duration=entry.get("duration"),
                uploader=entry.get("uploader"),
            )
        )

    return videos
