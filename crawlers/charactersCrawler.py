from marvel.marvel import Marvel
import os
import json


class charactersCrawler:
    def __init__(
        self,
        PUBLIC_KEY: str,
        PRIVATE_KEY: str,
        num_total: int,
        limit: int,
        output_dir: str,
    ):
        self.public_key = PUBLIC_KEY
        self.private_key = PRIVATE_KEY
        self.num_needed = num_total
        self.offset = 0
        self.limit = limit
        self.output_dir = output_dir
        self.m = Marvel(
            PUBLIC_KEY=self.public_key, PRIVATE_KEY=self.private_key, LIMIT=self.limit
        )
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
