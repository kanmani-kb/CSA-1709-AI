
from sklearn.tree import DecisionTreeClassifier

# Dataset
X = [
    [1, 1],
    [1, 0],
    [0, 1],
    [0, 0],
    [1, 1],
    [0, 0]
]

y = [1, 1, 1, 0, 1, 0]

# Create model
model = DecisionTreeClassifier()

# Train model
model.fit(X, y)

# Predict new data
prediction = model.predict([[1, 0]])

print("Prediction:", prediction[0])

if prediction[0] == 1:
    print("Result: Yes")
else:
    print("Result: No")
