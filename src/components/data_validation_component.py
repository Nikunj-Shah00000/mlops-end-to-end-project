import pandas as pd
import numpy as np

from src.logger import logging
from src.exception import CustomException

import os
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from pathlib import Path


@dataclass
class DataValidationConfig:
    pass

class DataValidation:
    def __init__(self):
        pass

    def initiate_data_validation(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise CustomException(e,sys)