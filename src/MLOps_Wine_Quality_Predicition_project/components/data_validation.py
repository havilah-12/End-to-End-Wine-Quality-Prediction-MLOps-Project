import os
from src.MLOps_Wine_Quality_Predicition_project import logger
from src.MLOps_Wine_Quality_Predicition_project.entity.config_entity import DataValidationConfig
import pandas as pd

# ----------- DataValidation -----------
class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
        
    def validate_all_columns(self) -> bool:
        try:
            data = pd.read_csv(self.config.unzip_data_dir)
            data_columns = set(data.columns)
            expected_columns = set(self.config.all_schema.keys())

            validation_status = data_columns == expected_columns

            with open(self.config.status_file, 'w') as f:
                f.write(f"Validation status: {validation_status}")

            return validation_status

        except Exception as e:
            raise RuntimeError(f"Error during validation: {e}")
