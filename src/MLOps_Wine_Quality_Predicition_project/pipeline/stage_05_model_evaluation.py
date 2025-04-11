from src.MLOps_Wine_Quality_Predicition_project.config.configuration import ConfigurationManager
from src.MLOps_Wine_Quality_Predicition_project.components.model_evalution import ModelEvaluation
from src.MLOps_Wine_Quality_Predicition_project import logger


STAGE_NAME = "Model Evaluation stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_evalution_config = config.get_model_evaluation_config()
        model_evalution_config  = ModelEvaluation( config = model_evalution_config)
        model_evalution_config.log_into_mlflow()

if __name__ == '__main__':
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
        data_transformation = ModelEvaluationTrainingPipeline()
        data_transformation.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nx============x")
        
    except Exception as  e:
        logger.exception(e)
        raise e    

