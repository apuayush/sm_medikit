"""
all routes
"""

from controllers import *

routes = [
    (r'/doc/login', Doctor.LoginHandler),
    (r'/doc/logout', Doctor.LogoutHandler),
    (r'/doc/profile', Doctor.ProfileViewer),
    (r'/pat/call', Patient.PatientHandler),
    (r'/eme', emergency.EmergencyHandler)
    # (r'/pat/recommend', recommendation.Recomendations)
]

