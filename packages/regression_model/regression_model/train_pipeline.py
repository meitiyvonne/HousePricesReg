import numpy as np
from sklearn.model_selection import train_test_split

from regression_model import pipeline
from regression_model.processing.data_management import load_dataset, save_pipeline
from regression_model.config import config
from regression_model import logger # <-- 導入日誌物件


def run_training() -> None:
    """Train the model."""

    # read training data
    data = load_dataset(file_name=config.TRAINING_DATA_FILE)

    # divide train and test
    X_train, X_test, y_train, y_test = train_test_split(
        data[config.FEATURES], data[config.TARGET], test_size=0.1, random_state=0
    )  # we are setting the seed here

    # transform the target
    y_train = np.log(y_train)

    # -- Logging: 記錄開始訓練和資料集大小 --
    logger.info(f"Training set size: {X_train.shape[0]}")
    logger.info(f"Target variable: {config.TARGET}")

    # fit model
    pipeline.price_pipe.fit(X_train[config.FEATURES], y_train)

    # -- Logging: 記錄模型訓練完成 --
    logger.info(f"Model version: {config.MODEL_VERSION}")
    logger.info(f"Pipeline name: {config.PIPELINE_NAME}")

    # persist trained pipeline
    save_pipeline(pipeline_to_persist=pipeline.price_pipe)


if __name__ == "__main__":
    run_training()