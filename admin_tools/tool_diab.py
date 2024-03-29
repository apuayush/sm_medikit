import sys
import pickle as pk
import numpy as np
# machine learning libraries

from sklearn.cross_validation import KFold   #For K-fold cross validation
from sklearn.ensemble import RandomForestClassifier

if sys.version_info[0] < 3:
    from Tkinter import *
else:
    from tkinter import *


class diabetes():

    def __init__(self):
        self.model = None

    def load_model(self):
        with open('../internal/diabetes/diabetes.pickle', 'rb') as f:
            self.model = pk.load(f)

    def predict(self, details):
        self.load_model()
        pred = self.model.predict_proba(details)

        return pred


    def output(self):

        out.delete(0, 'end')

        details = list()
        details.append(float(Pregnancies.get()))
        details.append(float(Glucose.get()))
        details.append(float(BloodPressure.get()))
        details.append(float(SkinThickness.get()))
        details.append(float(Insulin.get()))
        details.append(float(BMI.get()))
        details.append(float(DiabetesPedigreeFunction.get()))
        details.append(float(Age.get()))

        Pregnancies.delete(0, 'end')
        Glucose.delete(0, 'end')
        BloodPressure.delete(0, 'end')
        SkinThickness.delete(0, 'end')
        Insulin.delete(0, 'end')
        BMI.delete(0, 'end')
        DiabetesPedigreeFunction.delete(0, 'end')
        DiabetesPedigreeFunction.delete(0, 'end')
        Age.delete(0, 'end')

        pred = self.predict(np.array(details).reshape(1, -1))
        prob = pred[0,0]

        print(prob)
        #convert details to string
        out.insert(0, str(np.ceil((1 - prob) * 100).astype(int)))
        return pred


if __name__ == '__main__':
    bs = diabetes()
    main = Tk()
    main.resizable(0, 0)
    fnt = (None, 20)

    Label(main, text="Pregnancies", font=fnt).grid(row=0, column=0)
    Label(main, text="Glucose", font=fnt).grid(row=1, column=0)
    Label(main, text="BloodPressure", font=fnt).grid(row=2, column=0)
    Label(main, text="SkinThickness", font=fnt).grid(row=3, column=0)
    Label(main, text="Insulin", font=fnt).grid(row=4, column=0)
    Label(main, text="BMI", font=fnt).grid(row=5, column=0)
    Label(main, text="DiabetesPedigreeFunction", font=fnt).grid(row=6, column=0)
    Label(main, text="Age", font=fnt).grid(row=7, column=0)
    Label(main, text="probability", font=fnt).grid(row=10, column=0)

    Pregnancies = Entry(main, font=fnt)
    Pregnancies.grid(row=0, column=1)
    Glucose = Entry(main, font=fnt)
    Glucose.grid(row=1, column=1)
    BloodPressure = Entry(main, font=fnt)
    BloodPressure.grid(row=2, column=1)
    SkinThickness = Entry(main, font=fnt)
    SkinThickness.grid(row=3, column=1)
    Insulin = Entry(main, font=fnt)
    Insulin.grid(row=4, column=1)
    BMI = Entry(main, font=fnt)
    BMI.grid(row=5, column=1)
    DiabetesPedigreeFunction = Entry(main, font=fnt)
    DiabetesPedigreeFunction.grid(row=6, column=1)
    Age = Entry(main, font=fnt)
    Age.grid(row=7, column=1)
    out = Entry(main, font=fnt)
    out.grid(row=10, column=1)

    Button(main, text='Quit', bg='red', font=fnt, command=main.destroy).\
        grid(row=11, column=1, sticky=W, pady=4)
    Button(main, text='Output',bg='green', font=fnt, command=bs.output).\
        grid(row=9, column=1, sticky=W, pady=4)
    mainloop()
