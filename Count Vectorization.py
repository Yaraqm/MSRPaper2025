from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import FunctionTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

print(clf)
# Define words to boost and their corresponding boost factors
boost_words = {
    'bug': 1.5, 'crash': 1.0, 'error': 1.5, 'fail': 1.5, 'fix': 1.0, 
    'issue': 1.0, 'problem': 1.0, 'resolve': 0.8, 'deprecated': 1.5, 
    'unstable': 1.0, 'critical': 2.0, 'defect': 1.5, 'inconsistent': 2.0,
    'failure': 1.0, 'unresolved': 1.5, 'broken': 1.5,
    'faulty': 1.5, 'defective': 1.5, 'malfunction': 1.5
}


# Define specific words to include in the CountVectorizer vocabulary
custom_vocab = {
    'bug': 0, 'crash': 1, 'error': 2, 'fail': 3, 'fix': 4, 
    'issue': 5, 'problem': 6, 'resolve': 7, 'deprecated': 8, 
    'unstable': 9, 'critical': 10, 'defect': 11, 'inconsistent': 12, 
    'failure': 13, 'unresolved': 14, 'broken': 15,
    'faulty': 16, 'defective': 17, 'malfunction': 18
}

# Define the CountVectorizer with the custom vocabulary
count_vectorizer = CountVectorizer(vocabulary=custom_vocab)

# Create a function to boost specific words in the Count matrix
def boost_count(X, feature_names):
    df = pd.DataFrame(X.toarray(), columns=feature_names)
    for word, boost in boost_words.items():
        if word in df.columns:
            df[word] *= boost
    return df.values

# Define a function to apply boosting after fitting
def apply_boosting(X):
    feature_names = count_vectorizer.get_feature_names_out()
    return boost_count(X, feature_names)

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
        ('text', Pipeline(steps=[('count', count_vectorizer), ('boost', boost_transformer)]), 'Commit Messages')
    ]
)


model_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', clf)
])