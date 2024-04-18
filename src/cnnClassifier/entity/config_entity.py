from dataclasses import dataclass
from pathlib import Path

"""
dataclass module is introduced in Python 3.7 as a utility tool to make structured classes 
specially for storing data.
"""

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path