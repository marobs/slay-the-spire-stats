import json
import os

from models.run_data import parse_run_data
from models.run_statistics import RunStatistics


def convert_run_to_json(directory, filename) -> str:
    """
    Converts all .run files in the given directory to .json files.
    """
    updated_filename = os.path.splitext(filename)[0] + ".json"
    old_path = os.path.join(directory, filename)
    new_path = os.path.join(directory, updated_filename)
    os.rename(old_path, new_path)
    return updated_filename


def read_run_data(directory) -> RunStatistics:
    """
    Given a base directory, converts all .run files to .json files, reads them,
    converts them to RunData, and returns a list of them.
    """
    run_data = []

    for filename in os.listdir(directory):
        if filename.endswith(".run"):
            filename = convert_run_to_json(directory, filename)

        with open(os.path.join(directory, filename), 'r') as f:
            print(f"Reading file {filename}")
            run = parse_run_data(json.load(f))
            print("Read run successfully")
            run_data.append(run)

    return RunStatistics(run_data)
