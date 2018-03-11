import sys
import _pickle as pk
import numpy as np
# machine learning libraries

from sklearn.cross_validation import KFold   #For K-fold cross validation
from sklearn.ensemble import RandomForestClassifier

if sys.version_info[0] < 3:
    from Tkinter import *
else:
    from tkinter import *

class Main(object):
    def classification_model(model, data, predictors, outcome):
        model.fit(data[predictors], data[outcome])
        predictions = model.predict(data[predictors])
        accuracy = metrics.accuracy_score(predictions, data[outcome])
        print("Accuracy : %s" % "{0:.3%}".format(accuracy))

        # k-fold cross-validation with 5 folds
        kf = KFold(data.shape[0], n_folds=5)
        error = []
        for train, test in kf:
            # Filter training data
            train_predictors = (data[predictors].iloc[train, :])

            # The target we're using to train the algorithm.
            train_target = data[outcome].iloc[train]

            # Training the algorithm using the predictors and target.
            model.fit(train_predictors, train_target)

            # Record error from each cross-validation run
            error.append(model.score(data[predictors].iloc[test, :], data[outcome].iloc[test]))

            print("Cross-Validation Score : %s" % "{0:.3%}".format(np.mean(error)))

        # Fit the model again so that it can be refered outside the function:
        model.fit(data[predictors], data[outcome])


class bst_cancer(Main):

    def __init__(self):
        self.model = None

    def load_model(self):
        with open('../internal/bst_cancer/bst_cancer.pickle', 'rb') as f:
            self.model = pk.load(f)


    def predict(self, details):
        self.load_model()
        pred = self.model.predict_proba(details)
        print(pred)


    def output(self):
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
        self.predict(details)
        print(np.array(details))
        return details

if __name__ == '__main__':
    bs = bst_cancer()
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

    Button(main, text='Quit', bg='red', font=fnt, command=main.destroy).\
        grid(row=10, column=0, sticky=W, pady=4)
    Button(main, text='Output',bg='green', font=fnt, command=bs.output).\
        grid(row=10, column=1, sticky=W, pady=4)
    mainloop()
