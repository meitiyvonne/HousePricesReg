import pathlib

import regression_model


PACKAGE_ROOT = pathlib.Path(regression_model.__file__).resolve().parent
TRAINED_MODEL_DIR = PACKAGE_ROOT / "trained_models"
DATASET_DIR = PACKAGE_ROOT / "datasets"

# data
TESTING_DATA_FILE = "test.csv"
TRAINING_DATA_FILE = "train.csv"
TARGET = "SalePrice"


# variables
FEATURES = [
    "MSSubClass",
    "MSZoning",
    "Neighborhood",
    "OverallQual",
    "OverallCond",
    "YearRemodAdd",
    "RoofStyle",
    "MasVnrType",
    "BsmtQual",
    "BsmtExposure",
    "HeatingQC",
    "CentralAir",
    "1stFlrSF",
    "GrLivArea",
    "BsmtFullBath",
    "KitchenQual",
    "Fireplaces",
    "FireplaceQu",
    "GarageType",
    "GarageFinish",
    "GarageCars",
    "PavedDrive",
    "LotFrontage",
    # this one is only to calculate temporal variable:
    "YrSold",
]

# this variable is to calculate the temporal variable,
# can be dropped afterwards
DROP_FEATURES = "YrSold"

# numerical variables with NA in train set
NUMERICAL_VARS_WITH_NA = ["LotFrontage"]

# categorical variables with NA in train set
CATEGORICAL_VARS_WITH_NA = [
    "MasVnrType",
    "BsmtQual",
    "BsmtExposure",
    "FireplaceQu",
    "GarageType",
    "GarageFinish",
]

TEMPORAL_VARS = "YearRemodAdd"

# variables to log transform
NUMERICALS_LOG_VARS = ["LotFrontage", "1stFlrSF", "GrLivArea"]

# categorical variables to encode
CATEGORICAL_VARS = [
    "MSZoning",
    "Neighborhood",
    "RoofStyle",
    "MasVnrType",
    "BsmtQual",
    "BsmtExposure",
    "HeatingQC",
    "CentralAir",
    "KitchenQual",
    "FireplaceQu",
    "GarageType",
    "GarageFinish",
    "PavedDrive",
]

NUMERICAL_NA_NOT_ALLOWED = [
    feature
    for feature in FEATURES
    if feature not in CATEGORICAL_VARS + NUMERICAL_VARS_WITH_NA
]

CATEGORICAL_NA_NOT_ALLOWED = [
    feature for feature in CATEGORICAL_VARS if feature not in CATEGORICAL_VARS_WITH_NA
]

# ==============================================================================
# PARTIE-5: Mappage des variables ordinales (順序變數映射)
# ==============================================================================

# Variables to map and their corresponding mapping
QUAL_MAPPINGS = {
    "ExterQual": {"Ex": 5, "Gd": 4, "TA": 3, "Fa": 2, "Po": 1, "Missing": 0},
    "KitchenQual": {"Ex": 5, "Gd": 4, "TA": 3, "Fa": 2, "Po": 1, "Missing": 0},
    "FireplaceQu": {"Ex": 5, "Gd": 4, "TA": 3, "Fa": 2, "Po": 1, "Missing": 0, "NA": 0},
    "GarageFinish": {"Fin": 3, "RFn": 2, "Unf": 1, "Missing": 0, "NA": 0},
    "HeatingQC": {"Ex": 5, "Gd": 4, "TA": 3, "Fa": 2, "Po": 1, "Missing": 0},
    "PavedDrive": {"Y": 3, "P": 2, "N": 1, "Missing": 0},
    "BsmtQual": {"Ex": 5, "Gd": 4, "TA": 3, "Fa": 2, "Po": 1, "Missing": 0, "NA": 0},
    "BsmtExposure": {"Gd": 4, "Av": 3, "Mn": 2, "No": 1, "Missing": 0, "NA": 0},
    "BsmtCond": {"Ex": 5, "Gd": 4, "TA": 3, "Fa": 2, "Po": 1, "Missing": 0, "NA": 0},
    "GarageQual": {"Ex": 5, "Gd": 4, "TA": 3, "Fa": 2, "Po": 1, "Missing": 0, "NA": 0},
    "GarageCond": {"Ex": 5, "Gd": 4, "TA": 3, "Fa": 2, "Po": 1, "Missing": 0, "NA": 0},
}

# Variables to apply the mapping to
MAP_VARS = list(QUAL_MAPPINGS.keys())