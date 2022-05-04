from typing import List
import os


def getJsonFiles(inputJsonDir) -> List[str]:
    files = [
        os.path.join(inputJsonDir, file)
        for file in os.listdir(inputJsonDir)
        if "json" in file
    ]
    return files
