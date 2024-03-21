import numpy as np
import cv2
import keras
from keras.applications.resnet50 import ResNet50
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import LinearSVC, SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import GridSearchCV

# Function to extract image features using a pre-trained ResNet50 model
def extract_image_features(image_path):
    base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
    feature_extractor = Model(inputs=base_model.input, outputs=base_model.layers[-1].output)
    
    image = cv2.imread(image_path)
    image = cv2.resize(image, (224, 224))
    image = np.expand_dims(image, axis=0)
    image = preprocess_input(image)
    
    features = feature_extractor.predict(image)
    return features.flatten()

# Load image features and labels (replace with your actual data)
# For demonstration purposes, let's assume you have lists of image paths and corresponding labels
image_paths = ["path/to/image1.jpg", "path/to/image2.jpg", ...]
image_labels = [0, 1, ...]  # Example labels

X = np.array([extract_image_features(image_path) for image_path in image_paths])
y = np.array(image_labels)

# Split data into train and validation sets
X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2, random_state=42)

# Define classifiers
clfs = {
    'Linear SVM': LinearSVC(),
    'RBF SVM': SVC(kernel='rbf'), 
    'Random Forest': RandomForestClassifier(),
    'MLP': MLPClassifier()
}

# Evaluate each classifier
for name, clf in clfs.items():
    clf.fit(X_train, y_train)
    pred = clf.predict(X_valid)
    accuracy = accuracy_score(y_valid, pred)
    print(f'{name} accuracy: {accuracy*100:.2f}%')

# Hyperparameter tuning (Grid search on SVM)
params = {'C': [0.1, 1, 10], 'gamma': [0.0001, 0.001, 0.1]}
grid = GridSearchCV(SVC(kernel='rbf'), params, cv=5)
grid.fit(X_train, y_train)

print("Best params:", grid.best_params_)
print("Best score:", grid.best_score_)
