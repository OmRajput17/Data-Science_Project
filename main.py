from src.datacience import logger
from src.datacience.pipeline.data_ingestion import DataIngestionTrainingPipeline
from src.datacience.pipeline.data_validation import DataValidationTrainingPipeline

## Data Ingestion Stage
STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<< \n\n x----------------------------x")
    
except Exception as e:
    logger.exception(e)
    raise e

## Data Validation Stage
STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.initiate_data_validation() 
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<< \n\n x----------------------------x")
    
except Exception as e:
    logger.exception(e)
    raise e