from marvel.marvel import Marvel
import os
import json


class eventsCrawler:
    def __init__(
        self,
        PUBLIC_KEY: str,
        PRIVATE_KEY: str,
        num_total: int,
        limit: int,
        output_dir: str,
        need_all_available: bool,
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
        self.events = self.m.events
        self.need_all_available = need_all_available

    def get_data(self):
        if self.need_all_available:
            self.num_needed = self.events.all()["data"]["total"]

        for i in range(self.num_needed // self.limit + 1):
            all_events = self.events.all(offset=self.offset)
            self.save_data(all_events)
            self.offset += self.limit

    def save_data(self, all_events):
        os.makedirs(self.output_dir, exist_ok=True)
        output_path = os.path.join(self.output_dir, "{}.json".format(self.offset))
        outputFile = open(output_path, "w")
        all_events = json.dumps(all_events, indent=4)
        outputFile.write(all_events)
        outputFile.close()
