
from src.MLOps_Wine_Quality_Predicition_project import logger
from src.MLOps_Wine_Quality_Predicition_project.config.configuration import ConfigurationManager
from src.MLOps_Wine_Quality_Predicition_project.components.data_ingestion import DataIngestion


STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
            
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)  # Correcting object instantiation
        data_ingestion.download_file()  # Using the correct object
        data_ingestion.extract_zip_file()  # Using the correct object

    
   
        
        
if __name__ == '__main__':
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nx============x")
        
    except Exception as  e:
        logger.exception(e)
        raise e
        