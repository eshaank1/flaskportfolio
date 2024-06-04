# Import packages
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Load data from a CSV dataset fuke into a structure called DataFrame
price_data = pd.read_csv('realtor-data.csv')

# Drop rows with missing values in the 'price' column
price_data.dropna(subset=['price'], inplace=True)

# Select the columns 'bed', 'bath', 'acre_lot' to use for predicting 'price'.
# Convert their values to numbers and replace any missing/invalid entries with 0.
X = price_data[['bed', 'bath', 'acre_lot']].apply(pd.to_numeric, errors='coerce').fillna(0)
y = price_data['price'].apply(pd.to_numeric, errors='coerce').fillna(0)

# Split the data into 2 parts: 1 for training the model and 1 for testing predictions
# In my code, 70% of the data is used for training and the remaining 30% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create a machine learning model based on random forests, which is a method that uses multiple decision trees
rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)

# Teach the model to predict 'price' using the training data (70%)
rf_regressor.fit(X_train, y_train)

# Use the trained model to predict 'price' for the testing data (30%)
y_pred = rf_regressor.predict(X_test)

# Calculate and print the mean squared error for the model's predictions
# The mean squared error tells us how accurate the model predictions are, lower numbers are better.
mse = mean_squared_error(y_test, y_pred)
print('Model MSE:', mse)

# This is a Flask web server app, so no need to save trained model to a file