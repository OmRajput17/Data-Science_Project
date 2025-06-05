import os
from sklearn.model_selection import train_test_split
import pandas as pd
from src.datacience import logger 
from src.datacience.entity.config_entity import (DataTransformationConfig)

class DataTransformation:
    def __init__(self, config:DataTransformationConfig):
        self.config = config

    ## Note : You can add different data Transformation Techniques like Scaler, PCA,etc.
    # You can perform all kind of EDA in ML cycle here before Passing this data to the model

    #Performing only train and test split bcoz data is already cleaned

    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)

        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Splitted data into training and testing set")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)