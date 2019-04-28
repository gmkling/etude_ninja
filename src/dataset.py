"""
dataset.py

Functions to perform certain operations on datasets.
Automates the creation of some folders and files for a dataset.

  ../datasets/<DATASET_NAME>
        ├── <DATASET_NAME>.md (Info about a dataset)
        ├── dataset_info.csv
        ├── recordings
        │   ├── audio_info.csv (basically the whole table minus audio/midi data)
        │   ├── audio_files...
        │   ├── midi_files...
        │    └...
        │
        ├── score_data (this is a bit undefined as yet)
            ├── score_info.csv
            ├── notation_files (optional) ...
            ├── midi_files...
            └...

"""

from database.sodb import Sodb, sodb_sf_data, sodb_recordings, sodb_notes, sodb_music, sodb_annotations

class Dataset:
    def __init__(self):



def create_dataset(datesetPath: str, datasetName: str):
    """
    Factory function for Dataset.
    Starts the process of creating a dataset
    :param datasetName: the name of the dataset to create
    :param instrumentName: the name of the instrument captured
    :return: a Dataset object
    """

def main():

if __name__ == '__main__':
    main()
