import pandas as pd
import typing as t

from regression_model.config import config


def validate_inputs(input_data: pd.DataFrame) -> t.Tuple[pd.DataFrame, t.Dict]:
    """Check model inputs for issues and return validated dataframe
    and errors dictionary."""

    # 複製輸入數據，避免修改原始數據
    validated_data = input_data.copy()
    errors = {}

    # --- 1. 檢查是否有缺失的必要特徵 ---
    # 這裡我們只檢查模型需要的特徵是否都在輸入數據中
    missing_cols = [
        col for col in config.FEATURES if col not in validated_data.columns
    ]

    if missing_cols:
        errors["missing_columns"] = [
            f"Required column '{col}' is missing." for col in missing_cols
        ]
        # 如果有核心特徵缺失，我們應該停止並返回 None
        return None, errors

    # --- 2. 檢查關鍵特徵是否有 NaN ---
    # 檢查用於時間計算的 'YrSold' 是否有缺失值 (因為它被用來計算 TemporalVariable)
    if validated_data[config.DROP_FEATURES].isnull().any():
        errors["temporal_variable_na"] = "The 'YrSold' variable, used for temporal calculation, contains missing values."
    
    # --- 3. 檢查數值變數是否符合預期 (簡化) ---
    # 檢查所有數值變數（包括離散數值）是否能夠轉換為數字類型
    numerical_check_vars = config.NUMERICAL_VARIABLES + config.DISCRETE_VARIABLES
    
    for var in numerical_check_vars:
        if var in validated_data.columns and not pd.api.types.is_numeric_dtype(validated_data[var]):
            # 嘗試強制轉換為數字，如果失敗則記錄錯誤
            try:
                validated_data[var] = pd.to_numeric(validated_data[var], errors='raise')
            except ValueError:
                errors[var] = f"Variable '{var}' should be numerical but contains non-numeric values."


    if errors:
        # 如果有錯誤，返回 None 和錯誤字典
        return None, errors
    
    # 如果沒有錯誤，返回乾淨的數據框
    return validated_data, errors