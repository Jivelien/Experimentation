from sklearn.datasets import load_wine
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd

X,y = load_wine(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)


lr = LogisticRegression()
model = lr.fit(X_train, y_train)
rf_predictions = model.predict(X_test)
df = pd.DataFrame(list(zip(rf_predictions, y_test)))
df['match'] = df[0] == df[1]

success = sum(df['match'])/len(df)


# complete missing value with mean
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='mean')
X_train_clean = imputer.fit(X_train)


from sklearn.metrics import classification_report

print(classification_report(rf_predictions, y_test))


from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier()
rf_model = rf.fit(X_train, y_train)
rf_predictions = rf_model.predict(X_test)

param_grid = { 
    'n_estimators': [200, 500],
    'max_features': ['auto', 'sqrt', 'log2'],
    'max_depth' : [4,5,6,7,8],
    'criterion' :['gini', 'entropy']
}
from sklearn.model_selection import GridSearchCV
CV = GridSearchCV(rf, param_grid, n_jobs= 8)
                  
CV.fit(X_train, y_train)  
print(CV.best_params_)    
print(CV.best_score_)


from sklearn.pipeline import Pipeline
pipe = Pipeline([('imputer', SimpleImputer()), ('rf', RandomForestClassifier())])
pipeline_model = pipe.fit(X_train, y_train)
pipeline_model.score(X_test, y_test)



import matplotlib.pyplot as plt 
from sklearn import metrics
#◘not working
metrics.plot_roc_curve(rf, X_test, y_test)
plt.show()



import matplotlib.pyplot as plt 
from sklearn import metrics, model_selection
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.datasets import load_breast_cancer

X,y = load_breast_cancer(return_X_y = True)

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, random_state=0)
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

plot_tree(clf, filled=True)
plt.show()