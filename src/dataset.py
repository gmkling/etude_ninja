"""
dataset.py

Functions to perform certain operations on datasets.
Automates the creation of some folders and files for a dataset.

  ../datasets/<DATASET_NAME>
        ├── <DATASET_NAME>.md (Info about a dataset)
        ├── dataset_info.csv
        ├── audio
        │   ├── audio_info.csv
        │   ├── audio_files...
        │   └...
        │
        ├── score_data (this is a bit undefined as yet)
        │   ├── score_info.csv
        │   ├── notation_files...
        │   ├── score_files...
        │   └...
        │
        └── midi_files (transcriptions of audio data)
            ├── midi_info.csv
            ├── midi_files...
            └...
"""

class Dataset:
    def __init__(self):



def create_dataset(datasetName: str):
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
