from sklearn.pipeline import Pipeline

import packages.regression_model.regression_model.processing.preprocessors as pp


CATEGORICAL_VARS = ['MSZoning',
                    'Neighborhood',
                    'RoofStyle',
                    'MasVnrType',
                    'BsmtQual',
                    'BsmtExposure',
                    'HeatingQC',
                    'CentralAir',
                    'KitchenQual',
                    'FireplaceQu',
                    'GarageType',
                    'GarageFinish',
                    'PavedDrive']

PIPELINE_NAME = 'lasso_regression'

price_pipe = Pipeline(
    [
        ('categorical_imputer',
         pp.CategoricalImputer(variables=CATEGORICAL_VARS)),
    ])
