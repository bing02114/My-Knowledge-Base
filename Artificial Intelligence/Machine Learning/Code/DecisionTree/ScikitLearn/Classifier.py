# 1. Import necessary libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# 2. Load the data
# The Iris dataset has 3 classes (species of iris) and 4 features.
iris = load_iris()
X, y = iris.data, iris.target

# 3. Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 4. Instantiate and train the model
# We set random_state for reproducibility
model_clf = DecisionTreeClassifier(max_depth=3, random_state=42)
model_clf.fit(X_train, y_train)

# 5. Make predictions on the test set
y_pred = model_clf.predict(X_test)

# 6. Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
print(f"Decision Tree Classifier Accuracy: {accuracy:.4f}\n")
print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))