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
        self.events = self.m.events

    def getEventsList(self):
        file = open(self.combinedJsonDir, "r")
        data = json.load(file)
        self.events_list = [
            data["results"][i]["id"] for i in range(len(data["results"]))
        ]
        file.close()
        return self.events_list

    def getCharacters(self, eventID: int):
        """
        Get characters for only one event
        :param eventID: eventID
        :return: list of characters for this certain event
        """
        offset = 0
        characters = list()
        total_num = self.events.characters(eventID)["data"]["total"]
        for i in range(total_num // self.limit + 1):
            data = self.events.characters(eventID, offset=offset)
            characters += [
                data["data"]["results"][_]["id"]
                for _ in range(len(data["data"]["results"]))
            ]
            offset += self.limit
        return characters
