import os
import yaml
from box import Box
from pathlib import Path
from ensure import ensure_annotations
from box.exceptions import BoxValueError
from src.datacience import logger
import json
import joblib
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> Box:
    """
    Reads YAML file and returns Box object (dot-accessible dictionary).

    Args:
        path_to_yaml (Path): Path to YAML file.

    Raises:
        ValueError: If yaml file is empty.

    Returns:
        Box: Dot-accessible config object.
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            if not content:
                raise ValueError("Yaml file is empty.")
            logger.info(f"Yaml file {path_to_yaml} loaded successfully.")
            return Box(content)
    
    except BoxValueError:
        raise ValueError("Yaml file is empty.")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):
    """
    Create list of directories

    Args:
        path_to_directories (list) : list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Derfaults to 
    """

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created Directory at : {path}")

@ensure_annotations
def save_json(path: Path, data:dict):
    """
    save json data
    Args:
        path (Path) : path to json file
        data (dict) : data to saved in json file
    """

    with open(path, 'w') as file:
        json.dump(data, file, indent=4)

    logger.info(f"json file saved at : {path}")

@ensure_annotations
def load_json(path: Path) -> Box:
    """
    load json data
    Args:
        path (Path) : path to json file

    Return:
        Box : Data as class attribute instad of dict
    """

    with open(path) as file:
        content = json.load(file)

    logger.info(f"json file loaded successfully from  : {path}")
    return Box(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Save binary file  
    Args:
        data(Any): Data to be saved as binary
        path(path): path to binary file
    """

    joblib.dump(value=data, filename=path)
    logger.info(f"Binary File saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Load binary file  
    Args:
        path(path): path to binary file

    Returns:
        Any: object stored in the file
    """

    data = joblib.load(path)
    logger.info(f"Binary File loaded from: {path}")
    return data