from crawlers.Base import CrawlerBase
import json


class events2charactersCrawler(CrawlerBase):
    def __init__(
        self,
        PUBLIC_KEY: str,
        PRIVATE_KEY: str,
        limit: int,
        combinedJsonDir: str,
        csvOutputPath: str,
    ):
        super().__init__(PUBLIC_KEY, PRIVATE_KEY, limit)
        self.combinedJsonDir = combinedJsonDir
        self.csvOutputPath = csvOutputPath
        self.events_list = None

    def getEventsList(self):
        file = open(self.combinedJsonDir, "r")
        data = json.load(file)
        self.events_list = [
            data["results"][i]["id"] for i in range(len(data["results"]))
        ]
        file.close()
        return self.events_list
