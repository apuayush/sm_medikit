"""
all routes
"""

from controllers import *

routes = [
    (r'/doc/login', Doctor.LoginHandler),
    (r'/doc/logout', Doctor.LogoutHandler),
    (r'/doc/profile', Doctor.ProfileViewer),
    (r'/pat/call', Patient.PatientHandler),
    (r'/pat/recommend', Patient.Recomendations)
]

