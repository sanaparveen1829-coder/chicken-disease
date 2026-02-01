import os
from box.exceptions import BoxValueError
import yaml
from CNNClassifier import logger
import json
from pathlib import Path
import joblib
from ensure import ensure_annotations
#from typing import Any
from typing import Union
from box import ConfigBox
import base64


@ensure_annotations
def read_yaml(path_to_yaml: Path) ->ConfigBox:
    """Reads a yaml file and returns

    Args:
        path_to_yaml (Path): Path to yaml file

    Returns:
        config_box: config_box type object
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as box_exception:
        raise ValueError("yaml file is empty or invalid")
    except Exception as e:
        logger.error(f"Error occurred while reading yaml file: {e}")
        raise e 
    

def create_directories(path_to_directories: list, verbose=True):
    """Creates list of directories

    Args:
        path_to_directories (list[Path]): List of directory paths
    """
    for path_to_directory in path_to_directories:
        os.makedirs(path_to_directory, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path_to_directory}")

@ensure_annotations
def save_json(path: Path, data):
    """Saves data in json format

    Args:
        path (Path): Path to json file
        data (Any): Data to be saved
    """
    try:
        with open(path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        logger.info(f"Data successfully saved to {path}")
    except Exception as e:
        logger.error(f"Error occurred while saving data to json file: {e}")
        raise e
    
@ensure_annotations
def load_json(path: Path):
    """Loads data from json file

    Args:
        path (Path): Path to json file
    Returns:


        Any: Data loaded from json file
    """
    try:
        with open(path) as json_file:
            data = json.load(json_file)
        logger.info(f"Data successfully loaded from {path}")
        return data
    except Exception as e:
        logger.error(f"Error occurred while loading data from json file: {e}")
        raise e
    
@ensure_annotations
def save_bin(data, path: Path) ->None:
    """Saves binary data to a file

    Args:
        data (Any): Data to be saved
        path (Path): Path to the binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary data successfully saved to {path}")

@ensure_annotations
def load_bin(path: Path) :
    """Loads binary data from a file

    Args:
        path (Path): Path to the binary
    Returns:

        Any: Data loaded from the binary file
    """
    data = joblib.load(filename=path)
    logger.info(f"Binary data successfully loaded from {path}")
    return data

@ensure_annotations
def get_size(path: Path) ->str:
    """Gets size of file in KB

    Args:
        path (Path): Path to the file
    Returns:
        str: Size of file in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    logger.info(f"File size for {path} is {size_in_kb} KB")
    return f"~{size_in_kb} KB"


@ensure_annotations
def encode_image_to_base64(image_path: Path) ->str:
    """Encodes an image to base64 format

    Args:
        image_path (Path): Path to the image file
    Returns:
        str: Base64 encoded string of the image
    """
    try:
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        logger.info(f"Image at {image_path} successfully encoded to base64")
        return encoded_string
    except Exception as e:
        logger.error(f"Error occurred while encoding image to base64: {e}")
        raise e
    

@ensure_annotations
def decode_base64_to_image(base64_string: str, output_path: Path):
    """Decodes a base64 string and saves it as an image file

    Args:
        base64_string (str): Base64 encoded string of the image
        output_path (Path): Path to save the decoded image file
    """
    img_data = base64.b64decode(base64_string)
    try:
        with open(output_path, "wb") as image_file:
            image_file.write(img_data)
        logger.info(f"Base64 string successfully decoded and saved to {output_path}")
    except Exception as e:
        logger.error(f"Error occurred while decoding base64 string to image: {e}")
        raise e
    
    