from crawlers.Base import CrawlerBase
import os
import json


class events2charactersCrawler(CrawlerBase):
    def __init__(
        self,
        PUBLIC_KEY: str,
        PRIVATE_KEY: str,
        limit: int,
        combinedJsonDir: str,
        csvOutputPath: str,
        resume_event_id=None,
    ):
        """
        Crawl the characters of the events
        :param PUBLIC_KEY: Marvel development portal public key
        :param PRIVATE_KEY: Marvel development portal private key
        :param limit: The highest volume be crawled in each request
        :param combinedJsonDir: Directory of the combined json file contained events ID
        :param csvOutputPath: Output directory of CSV file
        :param resume_event_id: The event ID where need to be resumed, is useful when the crawling process is interrupted
        """
        super().__init__(PUBLIC_KEY, PRIVATE_KEY, limit)
        self.combinedJsonDir = combinedJsonDir
        self.csvOutputPath = csvOutputPath
        self.events = self.m.events
        self.resume_event_id = resume_event_id

    def getEventsList(self):
        """
        Get a list of events ID from the combined json file
        :return: events list
        """
        file = open(self.combinedJsonDir, "r")
        data = json.load(file)
        events_list = [data["results"][i]["id"] for i in range(len(data["results"]))]
        events_list.sort()
        file.close()
        return events_list

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

    def CSVinit(self):
        os.makedirs(self.csvOutputPath, exist_ok=True)
        csvPath = os.path.join(self.csvOutputPath, "event2characters.csv")
        csvfile = open(csvPath, "w")
        csvfile.write("eventID,characterID\n")
        csvfile.close()

    def writeCSV(self, eventID, charactersList):
        os.makedirs(self.csvOutputPath, exist_ok=True)
        csvPath = os.path.join(self.csvOutputPath, "event2characters.csv")
        csvfile = open(csvPath, "a")
        for ch in charactersList:
            csvfile.write("{},{}\n".format(eventID, ch))
        csvfile.close()

    def get_write_data(self):
        events_list = self.getEventsList()
        if self.resume_event_id is None:
            self.CSVinit()
            for eventid in events_list:
                charactersList = self.getCharacters(eventID=eventid)
                self.writeCSV(eventID=eventid, charactersList=charactersList)
        else:
            curIndex = events_list.index(self.resume_event_id)
            for i in range(curIndex + 1, len(events_list)):
                eventid = events_list[i]
                charactersList = self.getCharacters(eventID=eventid)
                self.writeCSV(eventID=eventid, charactersList=charactersList)
