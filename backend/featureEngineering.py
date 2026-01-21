from sklearn.base import BaseEstimator, TransformerMixin

def getLastLetter(df):
    df['lastLetter'] = [name[-1] for name in df['firstName']]
    return df

class FeatureEngineering(BaseEstimator, TransformerMixin):
    def __init__(self, transformers):
        self.transformers = transformers

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        for name, transformer in self.transformers:
            X = transformer.transform(X)
        return X