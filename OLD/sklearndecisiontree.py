from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, precision_score, recall_score

data = pd.read_csv(
    'https://raw.githubusercontent.com/jayelm/decisiontrees/master/example_data/breast-cancer-testing.csv')
X = data.drop(['4'], axis=1)
y = data['4']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print(data.describe())
decision_tree = DecisionTreeClassifier(random_state=0, max_depth=3)
train_model_DT = decision_tree.fit(X_train, y_train)
y_pred_DT = train_model_DT.predict(X_test)
DT_accuracy = accuracy_score(y_test, y_pred_DT)
DT_confusion = confusion_matrix(y_test, y_pred_DT)
DT_f1 = f1_score(y_test, y_pred_DT, average='macro')
DT_precision = precision_score(y_test, y_pred_DT, average='macro')
DT_recall = recall_score(y_test, y_pred_DT, average='macro')
error_rate = 1 - DT_accuracy
print('DT_accuracy:', DT_accuracy)
print('DT_f1:', DT_f1)
print('DT_precision:', DT_precision)
print('DT_recall:', DT_recall)
print('Error_rate:', error_rate)
print('DT_confusion:', DT_confusion)
