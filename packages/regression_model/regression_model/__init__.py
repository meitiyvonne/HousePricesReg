import logging


# Version of the package
__version__ = "0.0.1" 
# 這裡的版本號是為了讓 config.py 成功導入 regression_model

# 確保預測結果可以從頂層套件導入
from .predict import make_prediction