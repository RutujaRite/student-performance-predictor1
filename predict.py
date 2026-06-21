import pickle


# Load Saved Model
with open("model/student_model.pkl", "rb") as file:
    model = pickle.load(file)


print("\n===== Student Performance Predictor =====\n")


study_hours = float(
    input("Enter Study Hours: ")
)

attendance = float(
    input("Enter Attendance Percentage: ")
)

previous_marks = float(
    input("Enter Previous Marks: ")
)

assignment_score = float(
    input("Enter Assignment Score: ")
)

sleep_hours = float(
    input("Enter Sleep Hours: ")
)


prediction = model.predict([
    [
        study_hours,
        attendance,
        previous_marks,
        assignment_score,
        sleep_hours
    ]
])


print(
    "\nPredicted Final Score:",
    round(prediction[0], 2)
)


if prediction[0] >= 80:
    print("Grade : A")

elif prediction[0] >= 60:
    print("Grade : B")

elif prediction[0] >= 40:
    print("Grade : C")

else:
    print("Grade : D")