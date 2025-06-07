from src.datacience.config.configuration import ConfigurationManager
from src.datacience.components.model_evaluation import ModelEvaluator
from src.datacience import logger

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluator(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()
