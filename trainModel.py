import pandas as pd

from sklearn.linear_model import LinearRegression

import pickle


# Load Dataset
data = pd.read_csv("data/student_data.csv")


# Input Features
X = data[
    [
        "Study_Hours",
        "Attendance",
        "Previous_Marks",
        "Assignment_Score",
        "Sleep_Hours"
    ]
]


# Output Column
y = data["Final_Score"]


# Create Model
model = LinearRegression()


# Train Model
model.fit(X, y)


# Save Model
with open("model/student_model.pkl", "wb") as file:
    pickle.dump(model, file)


print("Model Trained Successfully")