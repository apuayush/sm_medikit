"""
all routes
"""

from controllers import *

routes = [
    (r'/agent/login', Doctor.LoginHandler),
    (r'/agent/logout', Doctor.LogoutHandler),
    (r'/agent/profile', Doctor.ProfileViewer),
    (r'/transaction/aadhar', parser.AadharAuthentication),
    (r'/agent/complaint', Complain.ComplainHandler)
]


