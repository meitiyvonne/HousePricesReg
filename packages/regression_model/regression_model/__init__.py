import logging


# Version of the package
__version__ = "0.0.1" 
# 這裡的版本號是為了讓 config.py 成功導入 regression_model

# 確保預測結果可以從頂層套件導入
from .predict_old import make_prediction

# 這是為了讓日誌物件可以在整個 package 中被導入
from regression_model.processing.utils import load_logger
# 導入 config 檔案中的 LOG_FILE_NAME
from regression_model.config import config

# 定義日誌物件，可以在任何地方導入 regression_model.logger 使用
logger = load_logger(log_file=config.LOG_FILE_NAME)

from regression_model.processing.utils import load_logger

__all__ = [
    'load_logger',
]