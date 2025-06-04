from src.datacience.config.configuration import ConfigurationManager
from src.datacience.components.data_validation import DataValidation
from src.datacience import logger


STAGE_NAME = 'Data Validation Stage'

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_validation(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_ingestion_config)
        data_validation.validate_all_column()


if __name__ == '__main__':
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        dataValidation = DataValidationTrainingPipeline()
        dataValidation.initiate_data_validation()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<< \n\n x----------------------------x")
    
    except Exception as e:
        logger.exception(e)
        raise e
                 
