from crawlers.eventsCrawler import eventsCrawler
from crawlers.utils.util import combine_jsonFiles
from crawlers.events2charactersCrawler import events2charactersCrawler


PUBLIC_KEY = "2c69de0f12c7f9d6406952e6aca6fab7"
PRIVATE_KEY = "1e7024cd196e873669e4782d9fa43db6bd181e9f"

evCrawler = eventsCrawler(
    PUBLIC_KEY=PUBLIC_KEY,
    PRIVATE_KEY=PRIVATE_KEY,
    num_total=20,
    limit=50,
    output_dir="./data/events/JSON/",
    need_all_available=True,
)

ev2ChCrawler = events2charactersCrawler(
    PUBLIC_KEY=PUBLIC_KEY,
    PRIVATE_KEY=PRIVATE_KEY,
    limit=50,
    combinedJsonDir="./data/events/JSON/combined/combined.json",
    csvOutputPath="./data/events/CSV/events_characters/",
)


if __name__ == "__main__":
    # Get all events and stored in json files
    evCrawler.get_data()

    # Combine all the crawled json files
    combine_jsonFiles(
        inputJsonDir="./data/events/JSON/",
        outputCombinedDir="./data/events/JSON/combined/",
    )

    # Get events to characters
    ev2ChCrawler.get_write_data()
