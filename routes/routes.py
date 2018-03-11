"""
all routes
"""

from controllers import *

routes = [
    (r'/doc/login', Doctor.LoginHandler),
    (r'/doc/logout', Doctor.LogoutHandler),
    (r'/doc/profile', Doctor.ProfileViewer)
]


