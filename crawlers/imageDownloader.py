import os
import json
from typing import List


class imageDownloader:
    def __init__(self, inputJsonDir: str, outputImageDir: str):
        self.inputJsonDir = inputJsonDir
        self.outputImageDir = outputImageDir
        self.jsonFiles = list()

    def getJsonFiles(self) -> List[str]:
        files = [
            os.path.join(self.inputJsonDir, file)
            for file in os.listdir(self.inputJsonDir)
            if "json" in file
        ]
        return files

    def getIDImageURL(self) -> dict:
        ID2ImageURL = dict()
        jsonFiles = self.getJsonFiles()
        for file_path in jsonFiles:
            file = open(file_path, "r")
            data = json.load(file)
            assert data["code"] == 200
            for i in range(len(data["data"]["results"])):
                ID2ImageURL[data["data"]["results"][i]["id"]] = "{}.{}".format(
                    data["data"]["results"][i]["thumbnail"]["path"],
                    data["data"]["results"][i]["thumbnail"]["extension"],
                )
        return ID2ImageURL

    def downloadAll(self):
        pass
