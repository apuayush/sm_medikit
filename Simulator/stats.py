from random import randint
from time import sleep
from pprint import pprint

# Oxygen >95%
# Respiratory rate 16 - 24
# Pulse 70 - 90

oxy = 97
resp = 20
pulse = 80
systolic = 110
diastolic = 70
chance = 5
out = {"systolic": systolic, "diastolic": diastolic, "bp_msg": "Ideal", "pulse": pulse, "pulse_msg": "Ideal", "resp": resp, "resp_msg": "Ideal", "oxygen_value": oxy, "oxy_msg": "Ideal"}

def change_size():
    val = randint(1, 100)
    if val<chance:
        return 1
    return 0

def change_small_bp():
    global systolic, diastolic
    systolic += randint(-1, 1)
    diastolic += randint(-1, 1)

def change_large_bp():
    global systolic, diastolic
    systolic = randint(70, 190)
    diastolic = randint(40, 100)

def bp():
    if change_size():
        change_large_bp()
    else:
        change_small_bp()

    if systolic<=90 and diastolic<=60:
        msg = "Low blood pressure"
    elif systolic<=120 and diastolic<=80:
        msg = "Ideal blood pressure"
    elif systolic<=140 and diastolic<=90:
        msg = "Pre-high blood pressure"
    else:
        msg = "High blood pressure"

    global out
    out["systolic"] = systolic
    out["diastolic"] = diastolic
    out["bp_msg"] = msg

def change_large_pulse():
    global pulse
    pulse = randint(25, 150)

def change_small_pulse():
    global pulse
    pulse += randint(-1, 1)

def pulse_value():
    if change_size():
        change_large_pulse()
    else:
        change_small_pulse()

    global pulse
    if pulse<70:
        msg = "Low"
    elif pulse<90:
        msg = "Ideal"
    else:
        msg = "High"

    global out
    out["pulse"] = pulse
    out["pulse_msg"] = msg

def change_small_resp():
    global resp
    resp += randint(-1, 1)/2.0

def change_large_resp():
    global resp
    resp = randint(12, 28)

def resp_value():
    if change_size():
        change_large_resp()
    else:
        change_small_resp()

    global resp
    if resp<16:
        msg = "Low"
    elif resp<24:
        msg = "Ideal"
    else:
        msg = "High"
    global out
    out["resp"] = resp
    out["resp_msg"] = msg

def oxy_value():
    global  oxy
    oxy += randint(-1, 1)/2.0
    if oxy>100:
        oxy = 100

    if oxy<95:
        msg = "Low"
    else:
        msg = "Ideal"
    global out
    out["oxygen_value"] = oxy
    out["oxy_msg"] = msg

while(True):
    bp()
    pulse_value()
    resp_value()
    oxy_value()
    pprint(out)
    sleep(2)
