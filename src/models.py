from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Video:
    title: str
    video_id: str
    webpage_url: str
    direct_url: Optional[str] = None
    duration: Optional[int] = None
    uploader: Optional[str] = None


@dataclass
class DownloadResult:
    source_url: str
    title: str
    videos: List[Video]
