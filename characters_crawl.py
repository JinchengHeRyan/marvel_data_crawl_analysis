from crawlers.charactersCrawler import charactersCrawler
from crawlers.imageDownloader import imageDownloader
from crawlers.utils.util import combine_jsonFiles


PUBLIC_KEY = "2c69de0f12c7f9d6406952e6aca6fab7"
PRIVATE_KEY = "1e7024cd196e873669e4782d9fa43db6bd181e9f"

chCrawler = charactersCrawler(
    PUBLIC_KEY=PUBLIC_KEY,
    PRIVATE_KEY=PRIVATE_KEY,
    num_total=2000,
    limit=50,
    output_dir="./data/characters/JSON/",
)

imageD = imageDownloader(
    inputJsonDir="./data/characters/JSON/", outputImageDir="./data/characters/images/"
)

if __name__ == "__main__":
    # Get all characters and stored in json files
    chCrawler.get_data()

    # Download character images
    imageD.downloadAll()

    # Combine all the crawled json files
    combine_jsonFiles(
        inputJsonDir="./data/characters/JSON/",
        outputCombinedDir="./data/characters/JSON/combined/",
    )

    # Transfer json to csv
    chCrawler.combinedJson2CSV(
        inputCombinedJson="./data/characters/JSON/combined/combined.json",
        outputCSVpath="./data/characters/CSV/",
    )
