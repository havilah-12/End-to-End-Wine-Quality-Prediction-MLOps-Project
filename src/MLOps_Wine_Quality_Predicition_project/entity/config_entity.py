from dataclasses import dataclass
from pathlib import Path
from typing import Dict



# ----------- Data Ingestion -----------
@dataclass(frozen = True)
class DataIngestionConfig:
    
    root_dir : Path
    source_URL : str
    local_data_file : Path
    unzip_dir: Path
    
    

# ----------- Data Validation -----------   
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    status_file: str
    unzip_data_dir: Path
    all_schema: Dict[str, any]
    local_data_file: Path


# ----------- Data Tansformation -----------
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
 
 

# -----------Model Training -----------
@dataclass
class ModelTrainerConfig:
    root_dir: str
    train_data_path: str
    test_data_path: str
    model_name: str
    alpha: float
    l1_ratio: float
    target_column: str
    
# -----------Model Evaluation -----------
@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    all_params: dict
    metric_file_name: Path
    target_column: str
    mlflow_uri: str