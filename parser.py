import json
import csv


DEFAULT_PATH_TO_SAVE_EXPORTED_DATA = "spotify_streaming_history.csv"


def parse_exported_data(filepath, save_to=DEFAULT_PATH_TO_SAVE_EXPORTED_DATA) -> None:
    with open(filepath, "r", encoding="utf-8") as file:
        streaming_history = json.load(file)


    with open(save_to, "w", newline="", encoding="utf-8") as file:
        fieldnames = streaming_history[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(streaming_history)
