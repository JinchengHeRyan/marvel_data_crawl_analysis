import json
from typing import List
import os


def getJsonFiles(inputJsonDir) -> List[str]:
    files = [
        os.path.join(inputJsonDir, file)
        for file in os.listdir(inputJsonDir)
        if "json" in file
    ]
    return files


def combine_jsonFiles(inputJsonDir, outputCombinedDir):
    combined = {"results": list()}
    files = getJsonFiles(inputJsonDir=inputJsonDir)
    for file_path in files:
        file = open(file_path, "r")
        data = json.load(file)
        combined["results"] += data["data"]["results"]
        file.close()

    os.makedirs(outputCombinedDir, exist_ok=True)
    output_path = os.path.join(outputCombinedDir, "combined.json")
    outputFile = open(output_path, "w")
    combined = json.dumps(combined, indent=4)
    outputFile.write(combined)
    outputFile.close()
