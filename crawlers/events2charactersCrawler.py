from crawlers.Base import CrawlerBase


class events2charactersCrawler(CrawlerBase):
    def __init__(self, PUBLIC_KEY: str, PRIVATE_KEY: str, limit: int):
        super().__init__(PUBLIC_KEY, PRIVATE_KEY, limit)
