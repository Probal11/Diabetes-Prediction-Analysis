import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
data=pd.read_csv('diabetes.csv')
X=data.drop('Outcome',axis='columns')
y=data.Outcome
X_train,X_test,y_train,y_test=train_test_split(X,y,train_size=0.2)
model=RandomForestClassifier(30)
model.fit(X_train,y_train)
preg=int(input("How many times have you been pregnant:"))
gluc=int(input("Glucose Concentration(Plasma glucose concentration a 2 hours in an oral glucose tolerance test):"))
Bp=int(input("Blood Pressure(Diastolic blood pressure (mm Hg)):"))
skin=int(input('Skin thickness(Triceps skin fold thickness (mm)):'))
insulin=int(input("Insulin(2-Hour serum insulin (mu U/ml)):"))
bmi=float(input("BMI(Body mass index (weight in kg/(height in m)^2)):"))
dia=float(input("Diabetes Pedigree Function:"))
Age=int(input("Age:"))
s=[preg,gluc,Bp,skin,insulin,bmi,dia,Age]
checker=pd.DataFrame([s])
prediction=model.predict(checker)
if 1 in prediction:
    print("You have diabetes")
else:
    print("You dont have diabetes")