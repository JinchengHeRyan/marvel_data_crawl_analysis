from crawlers.eventsCrawler import eventsCrawler
from crawlers.utils.util import combine_jsonFiles


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


if __name__ == "__main__":
    # Get all events and stored in json files
    evCrawler.get_data()

    # Combine all the crawled json files
    combine_jsonFiles(
        inputJsonDir="./data/events/JSON/",
        outputCombinedDir="./data/events/JSON/combined/",
    )
