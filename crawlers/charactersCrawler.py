from crawlers.Base import CrawlerBase
import os
import json


class charactersCrawler(CrawlerBase):
    def __init__(
        self,
        PUBLIC_KEY: str,
        PRIVATE_KEY: str,
        num_total: int,
        limit: int,
        output_dir: str,
    ):
        super().__init__(PUBLIC_KEY, PRIVATE_KEY, limit)
        self.num_needed = num_total
        self.offset = 0
        self.output_dir = output_dir
        self.characters = self.m.characters

    def get_data(self):
        for i in range(self.num_needed // self.limit):
            all_characters = self.characters.all(offset=self.offset)
            self.save_data(all_characters)
            self.offset += self.limit

    def save_data(self, all_characters):
        os.makedirs(self.output_dir, exist_ok=True)
        output_path = os.path.join(self.output_dir, "{}.json".format(self.offset))
        outputFile = open(output_path, "w")
        all_characters = json.dumps(all_characters, indent=4)
        outputFile.write(all_characters)
        outputFile.close()

    @staticmethod
    def combinedJson2CSV(inputCombinedJson: str, outputCSVpath: str):
        os.makedirs(outputCSVpath, exist_ok=True)
        csv_path = os.path.join(outputCSVpath, "all_characters.csv")
        csvfile = open(csv_path, "w")
        csvfile.write("id,name\n")

        json_file = open(inputCombinedJson, "r")
        data = json.load(json_file)
        for i in range(len(data["results"])):
            id = data["results"][i]["id"]
            name = data["results"][i]["name"]
            csvfile.write("{},{}\n".format(str(id), name))
        csvfile.close()
