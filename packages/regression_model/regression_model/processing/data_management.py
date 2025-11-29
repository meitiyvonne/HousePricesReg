import pandas as pd
import joblib
from pathlib import Path
import typing as t

from regression_model import __version__ as _version
from regression_model.config import config

# --- 設定檔案路徑 (從 config.py 取得) ---
PACKAGE_ROOT = config.PACKAGE_ROOT
TRAINED_MODEL_DIR = config.TRAINED_MODEL_DIR
DATASET_DIR = config.DATASET_DIR


def load_dataset(*, file_name: str) -> pd.DataFrame:
    """載入數據集."""
    # 這裡我們假設數據放在專案根目錄的 'datasets' 資料夾
    # 因為 config.py 的設置可能有點歧義，我們直接使用一個較安全的路徑
    
    # 修正：根據 config.py 的邏輯，如果 DATASET_DIR = PACKAGE_ROOT / "datasets"，
    # 且 PACKAGE_ROOT 是內層模組，則數據目錄在:
    # .../regression_model/regression_model/datasets
    
    # 為了簡化，我們將使用絕對路徑來讀取位於專案根目錄 (HousePricesReg/) 的 datasets/
    # 💡 最佳實踐：將 'datasets' 目錄放在 HousePricesReg/ 根目錄
    # 這裡我們將路徑調整為讀取專案根目錄下的 'datasets/'
    
    # 這是假設您的專案根目錄 (HousePricesReg) 有一個 datasets/ 資料夾
    # 您可能需要調整路徑，但先嘗試這個：
    file_path = Path.cwd() / "datasets" / file_name
    
    if not file_path.exists():
        # 如果找不到，嘗試使用 config 裡面的路徑
        file_path = DATASET_DIR / file_name
    
    data = pd.read_csv(file_path)
    return data


def save_pipeline(*, pipeline_to_persist) -> None:
    """儲存訓練好的模型 (Pipeline)."""
    
    # 由於 train_pipeline.py 只是調用了 save_pipeline，這裡提供完整實現
    save_file_name = f"lasso_regression_output_v{_version}.pkl"
    save_path = TRAINED_MODEL_DIR / save_file_name

    # 移除舊的模型檔案 (可選)
    remove_old_pipelines(files_to_keep=[save_file_name])
    
    joblib.dump(pipeline_to_persist, save_path)


def load_pipeline(*, file_name: str):
    """載入已儲存的模型 (Pipeline)."""
    
    # 由於 predict.py 依賴 'regression_model.pkl'，我們直接使用該名稱
    file_path = TRAINED_MODEL_DIR / file_name
    trained_pipeline = joblib.load(filename=file_path)
    return trained_pipeline


def remove_old_pipelines(*, files_to_keep: t.List[str]) -> None:
    """移除舊的模型 artifact."""
    
    do_not_delete = files_to_keep + ["__init__.py"]
    for model_file in TRAINED_MODEL_DIR.iterdir():
        if model_file.name not in do_not_delete:
            model_file.unlink()