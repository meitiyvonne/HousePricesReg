import numpy as np
import pandas as pd

from regression_model.processing.data_management import load_pipeline
from regression_model.config import config


pipeline_file_name = "regression_model.pkl"
_price_pipe = load_pipeline(file_name=pipeline_file_name)


def make_prediction(*, input_data) -> dict:
    """Make a prediction using the saved model pipeline."""

    data = pd.read_json(input_data)
    prediction = _price_pipe.predict(data[config.FEATURES])
    output = np.exp(prediction)
    response = {"predictions": output}

    return response
c:\Users\yvonne\Desktop\2024-S~1\420-A6~2\3ED42~1.PRE\3ED42~1.PRE\packages\REGRES~1\REGRES~1\TRAINE~1\REGRES~1.PKL