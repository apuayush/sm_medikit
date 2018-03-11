import matplotlib.pyplot as plt
import Tkinter
from random import randint
from time import sleep

systolic = 110
diastolic = 70
chance = 5

def output():
    if systolic<=90 and diastolic<=60:
        msg = "Low blood pressure"
    elif systolic<=120 and diastolic<=80:
        msg = "Ideal blood pressure"
    elif systolic<=140 and diastolic<=90:
        msg = "Pre-high blood pressure"
    else:
        msg = "High blood pressure"
    print str(systolic) + " / " + str(diastolic) + " " + msg

def change_small():
    global systolic, diastolic
    systolic += randint(-1, 1)
    diastolic += randint(-1, 1)

def change_large():
    global systolic, diastolic
    systolic = randint(70, 190)
    diastolic = randint(40, 100)


while(True):
    output()
    sleep(2)
    val = randint(1, 100)
    if val<chance:
        change_large()
    else:
        change_small()
