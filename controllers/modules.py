from tornado.web import RequestHandler, Application, removeslash
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import parse_command_line
from tornado.gen import coroutine

# other libraries
from bs4 import BeautifulSoup as soup
import sys
import jwt
import uuid
import json
import os
import base64
from datetime import datetime
import env
from motor import MotorClient
import json
from bson import json_util
import requests
import xmltodict
import time

# from firebase import firebase

# hash libraries
from hashlib import sha256
#
JWT_SECRET = env.JWT_SECRET
JWT_ALGORITHM = env.JWT_ALGORITHM
# db = MotorClient(env.db)['sm_medikit']
fb = firebase.FirebaseApplication(env.fb)
# JWT_SECRET = os.environ['JWT_SECRET']
# JWT_ALGORITHM = os.environ['JWT_ALGORITHM']
# db = MotorClient(os.environ['DB_LINK'])['sm_medikit']

Un = 1 # Unknown uid

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': env.pid,
})

db = firestore.client()