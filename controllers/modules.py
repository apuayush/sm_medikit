# Tornado libraries
from tornado.web import RequestHandler, Application, removeslash
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import parse_command_line
from tornado.gen import coroutine

import requests
import jwt
import time
import uuid
import os
import base64
from datetime import datetime
# import env
from motor import MotorClient
import json
from bson import json_util


import os
from controllers import env

from motor import MotorClient

# hash libraries
from hashlib import sha256

if os.environ.get('production'):
    JWT_SECRET = os.environ['JWT_SECRET']
    JWT_ALGORITHM = os.environ['JWT_ALGORITHM']
    PID = os.environ['PID']
    DB_link = os.environ['db']
    fb = os.environ['fb']
else:
    JWT_SECRET = env.JWT_SECRET
    JWT_ALGORITHM = env.JWT_ALGORITHM
    PID = env.pid
    DB_link = env.db
    fb = env.fb

db1 = MotorClient(DB_link)['sm_medikit']

Un = 1 # Unknown uid

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials
cred = credentials.Certificate("api.json")
firebase_admin.initialize_app(cred, {
  'projectId': PID,
})

db = firestore.client()

