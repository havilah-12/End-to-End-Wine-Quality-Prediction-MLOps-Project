from dataclasses import dataclass
from pathlib import Path
from typing import Dict

@dataclass(frozen = True)

class DataIngestionConfig:
    
    root_dir : Path
    source_URL : str
    local_data_file : Path
    unzip_dir: Path
    
    
    
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    status_file: str
    unzip_data_dir: Path
    all_schema: Dict[str, any]
    local_data_file: Path
