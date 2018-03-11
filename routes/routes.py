"""
all routes
"""

from controllers import *

routes = [
    (r'/login', Doctor.LoginHandler),
    (r'/logout', Doctor.LogoutHandler),
    (r'/eme', emergency.EmergencyHandler),
    (r'/recommend', recommendation.RecommendationHandler)
]

