from crawlers.charactersCrawler import charactersCrawler
from crawlers.imageDownloader import imageDownloader


PUBLIC_KEY = "2c69de0f12c7f9d6406952e6aca6fab7"
PRIVATE_KEY = "1e7024cd196e873669e4782d9fa43db6bd181e9f"

chCrawler = charactersCrawler(
    PUBLIC_KEY=PUBLIC_KEY,
    PRIVATE_KEY=PRIVATE_KEY,
    num_total=2000,
    limit=50,
    output_dir="./data/characters/",
)

imageD = imageDownloader(
    inputJsonDir="./data/characters", outputImageDir="./data/images/characters/"
)

if __name__ == "__main__":
    # Get all characters and stored in json files
    chCrawler.get_data()

    # Download character images
    imageD.downloadAll()
