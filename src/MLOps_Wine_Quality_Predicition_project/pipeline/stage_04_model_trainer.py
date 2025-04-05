from src.MLOps_Wine_Quality_Predicition_project.config.configuration import ConfigurationManager
from src.MLOps_Wine_Quality_Predicition_project.components.model_trainer import ModelTrainer
from src.MLOps_Wine_Quality_Predicition_project import logger
from pathlib import Path


STAGE_NAME = "Model Trainer stage"
class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config= model_trainer_config)
        model_trainer_config.train()

if __name__ == '__main__':
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
        data_transformation = ModelTrainerTrainingPipeline()
        data_transformation.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nx============x")
        
    except Exception as  e:
        logger.exception(e)
        raise e    

