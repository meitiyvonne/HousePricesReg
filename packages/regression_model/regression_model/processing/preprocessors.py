import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class CategoricalImputer(BaseEstimator, TransformerMixin):
    """Categorical data missing value imputer."""

    def __init__(self, variables=None) -> None:
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X: pd.DataFrame, y: pd.Series = None) -> 'CategoricalImputer':
        """Fit statement to accomodate the sklearn pipeline."""

        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        """Apply the transforms to the dataframe."""

        X = X.copy()
        for feature in self.variables:
            X[feature] = X[feature].fillna('Missing')

        return X

# ==============================================================================
# Mapper
# ==============================================================================
class Mapper(BaseEstimator, TransformerMixin):
    """
    Ordinal variable mapper.
    Used to convert categorical variables with ordinal nature into numerical values
    based on a provided mapping dictionary.
    """

    def __init__(self, variables=None, mappings=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

        self.mappings = mappings

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        # We store the mappings provided at initialization
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X = X.copy()
        for feature in self.variables:
            # Apply the mapping for the specific feature
            X[feature] = X[feature].map(self.mappings[feature])

        return X

# ==============================================================================
# WeirdRatio
# ==============================================================================
class WeirdRatio(BaseEstimator, TransformerMixin):
    """
    Custom Feature Creation: calculates a ratio between 1stFlrSF and GrLivArea.
    Creates a new feature: 'WeirdRatio'.
    """

    def __init__(self):
        # No variables needed for initialization
        pass

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X = X.copy()
        
        # We ensure no division by zero and handle NA values
        X['WeirdRatio'] = X['1stFlrSF'] / (X['GrLivArea'] + 1e-6)
        
        # Since 'WeirdRatio' is a new feature, we need to add it to the model's feature list in the config,
        # but for now, the pipeline will just use it. 
        # The training will fail later if not added to config.FEATURES.

        return X