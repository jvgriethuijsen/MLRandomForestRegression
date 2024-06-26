import pandas as pd, numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
#import setup # Truncate and regen DB
import util

teachers_df = pd.DataFrame(util.teachers_table.all())
schools_df = pd.DataFrame(util.schools_table.all())
feedback_df = pd.DataFrame(util.feedback_table.all())

data = feedback_df.merge(teachers_df, on='teacher_id').merge(schools_df, on='school_id')
categorical_columns = [
    'qualifications', 'subject_expertise', 'teaching_style', 'location_x',
    'location_y', 'availability', 'requirements', 'culture', 'salary_range', 'student_demographics'
]

categorical_columns = [col for col in categorical_columns if col in data.columns]
data = pd.get_dummies(data, columns=categorical_columns)
data = data.astype(int) # Convert bools to ints

X = data.drop(columns=['teacher_id', 'school_id', 'rating'])
y = data['rating']

#print("Data types in X:\n", X.dtypes) #Debug
#assert all(X.dtypes.apply(lambda dtype: np.issubdtype(dtype, np.number))), "Non-numeric columns found in X"

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

def predict_match(teacher_profile, school_profile):
    input_data = {**teacher_profile, **school_profile}
    input_data = pd.DataFrame([input_data])
    input_data = pd.get_dummies(input_data)
    input_data = input_data.reindex(columns=X.columns, fill_value=0)
    
    predicted_rating = model.predict(input_data)[0]
    return predicted_rating

# Export the model and prediction function
__all__ = ['predict_match']