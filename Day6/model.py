from pathlib import Path

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, root_mean_squared_error

from preprocessing import preprocess_data

current_dir = Path(__file__).parent  # Day6
data_path = current_dir.parent / "Day5" / "cleaned_student_performance.csv"

X_train, X_test, y_train, y_test, preprocessor = preprocess_data(data_path)

model = LinearRegression()
model.fit(X_train, y_train)

prediction = model.predict(X_test)

# pd.DataFrame(prediction, columns=['y_predicted'])
# y_test

print("Predicted:", prediction.round(2))
print("Actual:", y_test.values)

mse = mean_squared_error(y_test, prediction)
rmse = root_mean_squared_error(y_test, prediction)
r2 = r2_score(y_test, prediction)

print(f"Mean Squared Error: {mse:.2f}")
print(f"Root Mean Squared Error: {rmse:.2f}")
print(f"R2 Score: {r2:.2f}")

# r2 score tells that model explains about 74% of the variation in the target
# rmse shows predictions are, on average, off by about ~4.23 points from the actual value

train_predictions = model.predict(X_train)

mse_train = mean_squared_error(y_train, train_predictions)
rmse_train = root_mean_squared_error(y_train, train_predictions)
r2_train = r2_score(y_train, train_predictions)

print(f"Train MSE: {mse_train:.2f}")
print(f"Train RMSE: {rmse_train:.2f}")
print(f"Train R2: {r2_train:.2f}")