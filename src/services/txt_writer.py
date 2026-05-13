import os

from src.exceptions import WriterError
from src.utils import ensure_output_dir


def write_videos(videos, output_file: str):
    try:
        ensure_output_dir(os.path.dirname(output_file))
        with open(output_file, "w", encoding="utf-8") as f:
            for idx, video in enumerate(videos, start=1):
                f.write(f"{idx}. {video.title}\n")
                f.write(f"   Video ID: {video.video_id}\n")
                f.write(f"   Page URL: {video.webpage_url}\n")
                if video.direct_url:
                    f.write(f"   Direct URL: {video.direct_url}\n")
                if video.uploader:
                    f.write(f"   Uploader: {video.uploader}\n")
                if video.duration:
                    f.write(f"   Duration: {video.duration} sec\n")
                f.write("\n")
    except Exception as exc:
        raise WriterError(str(exc)) from exc
