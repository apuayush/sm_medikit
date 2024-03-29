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


class Bst_cancer():

    def __init__(self):
        self.model = None

    def load_model(self):
        with open('../internal/bst_cancer/bst_cancer.pickle', 'rb') as f:
            self.model = pk.load(f)

    def predict(self, details):
        self.load_model()
        pred = self.model.predict_proba(details)

        return pred


    def output(self):

        out.delete(0, 'end')

        details = list()
        details.append(float(radius_mean.get()))
        details.append(float(texture_mean.get()))
        details.append(float(perimeter_mean.get()))
        details.append(float(area_mean.get()))
        details.append(float(smoothness_mean.get()))
        details.append(float(compactness_mean.get()))
        details.append(float(concavity_mean.get()))
        details.append(float(concave.get()))
        details.append(float(symmetry_mean.get()))
        details.append(float(fractal_dimension_mean.get()))

        radius_mean.delete(0, 'end')
        texture_mean.delete(0, 'end')
        perimeter_mean.delete(0, 'end')
        area_mean.delete(0, 'end')
        smoothness_mean.delete(0, 'end')
        compactness_mean.delete(0, 'end')
        concavity_mean.delete(0, 'end')
        concavity_mean.delete(0, 'end')
        concave.delete(0, 'end')
        symmetry_mean.delete(0, 'end')
        fractal_dimension_mean.delete(0, 'end')

        pred = self.predict(np.array(details).reshape(1, -1))
        prob = pred[0,0]

        print(prob)
        #convert details to string
        out.insert(0, str(np.ceil((1 - prob) * 100).astype(int)))
        return pred


if __name__ == '__main__':
    bs = Bst_cancer()
    main = Tk()
    main.resizable(0, 0)
    fnt = (None, 20)

    Label(main, text="radius_mean", font=fnt).grid(row=0, column=0)
    Label(main, text="texture_mean", font=fnt).grid(row=1, column=0)
    Label(main, text="perimeter_mean", font=fnt).grid(row=2, column=0)
    Label(main, text="area_mean", font=fnt).grid(row=3, column=0)
    Label(main, text="smoothness_mean", font=fnt).grid(row=4, column=0)
    Label(main, text="compactness_mean", font=fnt).grid(row=5, column=0)
    Label(main, text="concavity_mean", font=fnt).grid(row=6, column=0)
    Label(main, text="concave points_mean", font=fnt).grid(row=7, column=0)
    Label(main, text="symmetry_mean", font=fnt).grid(row=8, column=0)
    Label(main, text="fractal_dimension_mean", font=fnt).grid(row=9, column=0)
    Label(main, text="probability", font=fnt).grid(row=11, column=0)

    radius_mean = Entry(main, font=fnt)
    radius_mean.grid(row=0, column=1)
    texture_mean = Entry(main, font=fnt)
    texture_mean.grid(row=1, column=1)
    perimeter_mean = Entry(main, font=fnt)
    perimeter_mean.grid(row=2, column=1)
    area_mean = Entry(main, font=fnt)
    area_mean.grid(row=3, column=1)
    smoothness_mean = Entry(main, font=fnt)
    smoothness_mean.grid(row=4, column=1)
    compactness_mean = Entry(main, font=fnt)
    compactness_mean.grid(row=5, column=1)
    concavity_mean = Entry(main, font=fnt)
    concavity_mean.grid(row=6, column=1)
    concave = Entry(main, font=fnt)
    concave.grid(row=7, column=1)
    symmetry_mean = Entry(main, font=fnt)
    symmetry_mean.grid(row=8, column=1)
    fractal_dimension_mean = Entry(main, font=fnt)
    fractal_dimension_mean.grid(row=9, column=1)
    out = Entry(main, font=fnt)
    out.grid(row=11, column=1)

    Button(main, text='Quit', bg='red', font=fnt, command=main.destroy).\
        grid(row=12, column=1, sticky=W, pady=4)
    Button(main, text='Output',bg='green', font=fnt, command=bs.output).\
        grid(row=10, column=1, sticky=W, pady=4)
    mainloop()
