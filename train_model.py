
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from imblearn.pipeline import make_pipeline
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, ExtraTreesClassifier
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from lightgbm import LGBMClassifier
from catboost import CatBoostClassifier
import pickle

# Load the dataset
data = pd.read_csv('diabetes_prediction_dataset.csv')

# Define categorical and numeric features
categorical_features = ['gender', 'smoking_history']
numeric_features = ['age', 'hypertension', 'heart_disease', 'bmi', 'HbA1c_level', 'blood_glucose_level']

# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(), categorical_features)
    ])

# Define features and target
X = data.drop('diabetes', axis=1)
y = data['diabetes']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define models and their parameter grids
models_and_params = {
    'RandomForest': (RandomForestClassifier(random_state=42), {
        'randomforestclassifier__n_estimators': [100, 200],
        'randomforestclassifier__max_depth': [10, 20, None]
    }),
    'GradientBoosting': (GradientBoostingClassifier(random_state=42), {
        'gradientboostingclassifier__n_estimators': [100, 200],
        'gradientboostingclassifier__learning_rate': [0.05, 0.1]
    }),
    'XGBoost': (XGBClassifier(eval_metric='mlogloss', random_state=42), {
        'xgbclassifier__n_estimators': [100, 200],
        'xgbclassifier__max_depth': [3, 5],
        'xgbclassifier__learning_rate': [0.05, 0.1]
    }),
    'ExtraTrees': (ExtraTreesClassifier(random_state=42), {
        'extratreesclassifier__n_estimators': [100, 200],
        'extratreesclassifier__max_depth': [10, 20, None]
    }),
    'LightGBM': (LGBMClassifier(random_state=42), {
        'lgbmclassifier__n_estimators': [100, 200],
        'lgbmclassifier__learning_rate': [0.05, 0.1]
    }),
    'CatBoost': (CatBoostClassifier(verbose=0, random_state=42), {
        'catboostclassifier__iterations': [100, 200],
        'catboostclassifier__learning_rate': [0.05, 0.1]
    })
}

# Iterate through models and perform training and evaluation
for model_name, (model, params) in models_and_params.items():
    pipeline = make_pipeline(preprocessor, SMOTE(random_state=42), model)
    clf = GridSearchCV(pipeline, params, cv=5, scoring='accuracy')
    clf.fit(X_train, y_train)
    best_model = clf.best_estimator_

    y_pred = best_model.predict(X_test)
    print(f"Results for {model_name}:")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))

    # Save each best model
    with open(f'best_{model_name}_model.pkl', 'wb') as file:
        pickle.dump(best_model, file)

print("All models trained and best models saved.")
