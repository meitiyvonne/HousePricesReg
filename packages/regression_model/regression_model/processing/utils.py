import logging
from logging.handlers import TimedRotatingFileHandler
import pathlib

from regression_model import config

# 定義日誌格式
FORMATTER = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - "
    "%(funcName)s:%(lineno)d - %(message)s"
)

# 定義日誌檔案路徑
LOG_DIR = config.PACKAGE_ROOT / 'logs'
LOG_DIR.mkdir(exist_ok=True)
FILE_PATH = LOG_DIR / config.LOG_FILE_NAME


def get_console_handler():
    # 創建一個處理器，將日誌輸出到控制台
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(FORMATTER)
    return console_handler


def get_file_handler(log_file):
    # 創建一個處理器，將日誌輸出到檔案中，每天輪替一次
    file_handler = TimedRotatingFileHandler(
        log_file, when='midnight', interval=1, backupCount=7
    )
    file_handler.setFormatter(FORMATTER)
    return file_handler


def load_logger(log_file=FILE_PATH, level=logging.INFO):
    """Factory to take care of setting up logging."""

    # 如果已經存在名為 'regression_model' 的日誌器，則使用現有的
    if "regression_model" in logging.Logger.manager.loggerDict:
        return logging.getLogger("regression_model")

    # 否則，創建新的日誌器
    logger = logging.getLogger("regression_model")
    logger.setLevel(level)
    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler(log_file))
    logger.propagate = False  # 防止日誌事件傳播到根日誌器
    return logger