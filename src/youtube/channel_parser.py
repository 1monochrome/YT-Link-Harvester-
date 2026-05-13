import re

from src.exceptions import InvalidChannelURLError

CHANNEL_REGEX = r"(https?:\/\/)?(www\.)?youtube\.com\/@([^\/\?\s]+)"


def extract_handle(channel_url: str) -> str:
    match = re.search(CHANNEL_REGEX, channel_url)

    if not match:
        raise InvalidChannelURLError(
            f"Invalid YouTube channel URL: {channel_url}"
        )

    return match.group(3)
