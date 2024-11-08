from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import FunctionTransformer 
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer

# Define words to boost and their corresponding boost factors
boost_words = {'bug': 1.5, 'crash': 1.0, 'error': 1.0, 'fail': 1.0, 'fix': 1.0, 'issue': 1.0, 'problem': 1.0, 'resolve': 1.0, 'deprecated': 1.0, 'unstable': 1.0, 'critical':1.0, 'defect': 1.0, 'inconsistent':1.0}

# Define the TF-IDF vectorizer
text_transformer = Pipeline(steps=[
    ('tfidf', TfidfVectorizer(max_features=1000))
])

# Fit the TF-IDF vectorizer on a sample of your data
text_transformer.fit(X_train['Commit Messages'])

# Create a function to boost specific words in the TF-IDF matrix
def boost_tfidf(X, feature_names):
    df = pd.DataFrame(X.toarray(), columns=feature_names)
    for word, boost in boost_words.items():
        if word in df.columns:
            df[word] *= boost
    return df.values

# Define a function to apply boosting after fitting
def apply_boosting(X):
    feature_names = text_transformer.named_steps['tfidf'].get_feature_names_out()
    return boost_tfidf(X, feature_names)

boost_transformer = FunctionTransformer(
    func=apply_boosting, 
    validate=False
)

# Define the numeric transformer
numeric_transformer = Pipeline(steps=[
    ('scaler', StandardScaler())
])


# Define the preprocessor
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, ['BUCKET_NAME', 'TEST_TOTAL', 'contains_unit', 'contains_fat', 'contains_java_filetype']),
        ('text', Pipeline(steps=[('tfidf', text_transformer), ('boost', boost_transformer)]), 'Commit Messages')
    ]
)

model_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', clf)
])