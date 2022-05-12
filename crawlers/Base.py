from marvel.marvel import Marvel


class CrawlerBase:
    def __init__(
        self,
        PUBLIC_KEY: str,
        PRIVATE_KEY: str,
        limit: int,
    ):
        """
        Base class for the crawlers
        :param PUBLIC_KEY: Marvel development portal public key
        :param PRIVATE_KEY: Marvel development portal private key
        :param limit: The highest volume be crawled in each request
        """
        self.public_key = PUBLIC_KEY
        self.private_key = PRIVATE_KEY
        self.limit = limit
        self.m = Marvel(
            PUBLIC_KEY=self.public_key, PRIVATE_KEY=self.private_key, LIMIT=self.limit
        )
