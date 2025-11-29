import io
import os
from pathlib import Path

from setuptools import find_packages, setup


# 獲取專案根目錄路徑
here = os.path.abspath(os.path.dirname(__file__))


# ----------------------------------------------------
# 1. 讀取版本號
#    這依賴於您在 regression_model/__init__.py 中設置了 __version__ 的邏輯
# ----------------------------------------------------
# 由於 VERSION 檔案放在 regression_model/ 目錄下，這樣讀取是正確的
try:
    with open(Path(here) / 'regression_model' / 'VERSION') as version_file:
        __version__ = version_file.read().strip()
except FileNotFoundError:
    # 如果找不到，設定一個後備版本號
    __version__ = '0.0.1' 


# ----------------------------------------------------
# 2. 導入外部依賴項 (從根目錄的 requirements.txt 讀取)
# ----------------------------------------------------
def list_reqs(fname='requirements.txt'):
    # 這裡直接讀取根目錄下的 requirements.txt
    with io.open(os.path.join(here, fname), encoding='utf-8') as f:
        return f.read().splitlines()

# 獲取 install_requires 列表
required = list_reqs(fname='requirements.txt')

# ====================================================
# 包的元數據 (Metadata)
# ====================================================
NAME = 'regression_model'
DESCRIPTION = 'Train and deploy a House Price prediction model.'
URL = 'https://github.com/your-username/your-repo'  # <-- 請替換
EMAIL = 'your-email@example.com'  # <-- 請替換
AUTHOR = 'Your Name'  # <-- 請替換
REQUIRES_PYTHON = '>=3.6.0'

setup(
    name=NAME,
    version=__version__,  # 使用讀取的版本號
    description=DESCRIPTION,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    # 查找所有 packages (除了 tests)
    packages=find_packages(exclude=('tests',)),
    # 確保 VERSION 文件被包含在 package 數據中
    package_data={'regression_model': ['VERSION']},
    # 設置依賴項
    install_requires=required,
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Trove classifiers (https://pypi.org/classifiers/)
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython'
    ],
)