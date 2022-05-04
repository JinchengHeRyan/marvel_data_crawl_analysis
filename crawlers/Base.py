from marvel.marvel import Marvel


class CrawlerBase:
    def __init__(
        self,
        PUBLIC_KEY: str,
        PRIVATE_KEY: str,
        limit: int,
    ):
        self.public_key = PUBLIC_KEY
        self.private_key = PRIVATE_KEY
        self.limit = limit
        self.m = Marvel(
            PUBLIC_KEY=self.public_key, PRIVATE_KEY=self.private_key, LIMIT=self.limit
        )
