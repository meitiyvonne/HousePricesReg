import numpy as np
import pandas as pd

from regression_model.processing.data_management import load_pipeline
from regression_model.processing.validation import validate_inputs  # <-- 新增：導入驗證函式
from regression_model.config import config


pipeline_file_name = "regression_model.pkl"
_price_pipe = load_pipeline(file_name=pipeline_file_name)


def make_prediction(*, input_data) -> dict:
    """Make a prediction using the saved model pipeline."""

    # 1. 將輸入數據從 JSON 轉換為 DataFrame
    data = pd.read_json(input_data)

    # 2. 執行輸入驗證
    validated_data, errors = validate_inputs(input_data=data)

    # 3. 處理驗證結果
    if errors:
        # 如果有錯誤，返回 None 和錯誤字典
        return {"predictions": None, "errors": errors}

    # 4. 進行預測
    # 注意：我們使用 validated_data 來進行預測
    prediction = _price_pipe.predict(validated_data[config.FEATURES])
    output = np.exp(prediction)

    # 5. 構建響應
    # 預測成功時，errors 字典是空的
    response = {"predictions": output, "errors": errors}

    return response