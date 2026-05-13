class YoutubeHarvesterError(Exception):
    pass


class DownloadError(YoutubeHarvesterError):
    pass


class ParseError(YoutubeHarvesterError):
    pass


class WriterError(YoutubeHarvesterError):
    pass
