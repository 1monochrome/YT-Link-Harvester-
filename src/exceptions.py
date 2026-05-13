class YoutubeFetcherError(Exception):
    """Base application exception."""


class InvalidChannelURLError(YoutubeFetcherError):
    """Raised when channel URL is invalid."""


class FeedFetchError(YoutubeFetcherError):
    """Raised when RSS feed fetch fails."""
