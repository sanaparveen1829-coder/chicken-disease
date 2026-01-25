import os
import urllib.request
import zipfile
from CNNClassifier import logger
from CNNClassifier.utils.common import get_size
from CNNClassifier.entity.config_entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        logger.info("Starting data download...")
        if not os.path.exists(self.config.local_data_file):
            filename, headers = urllib.request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file,
            )
            logger.info(
                f"Data downloaded successfully! and saved at {self.config.local_data_file} "
                f"and the file size is {get_size(Path(filename))}"
            )
        else:
            logger.info(f"File already exists of size: {get_size(self.config.local_data_file)}")

    def extract_zip_file(self):
        logger.info("Starting data extraction...")
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_path)