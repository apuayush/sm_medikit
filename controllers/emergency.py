from controllers.modules import *
from controllers.utility import *
from tornado.httputil import parse_body_arguments
from urllib.parse import parse_qs


class EmergencyHandler(RequestHandler):

    def set_default_headers(self):
        print("setting headers!!!")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Content-type', 'application/json')

    def options(self):
        # no body
        self.set_status(204)
        self.finish()

    # emergency admissions
    def post(self):
        # data = parse_qs(self.request.body.decode('utf-8'))
        data = json.loads(self.request.body.decode('utf-8'))

        # uid = self.get_argument('phone')
        # pname = self.get_argument('name')
        # gps = self.get_argument('gps')
        # gend = self.get_argument('gender')
        # description = self.get_argument('description')

        uid = data['phone']
        pname = data['name']
        gps = data['gps']
        gend = data['gender']
        description = data['description']
        image = data['image']

        if len(uid) == 0:
            Un += 1

            uid = '0' * (10 - len(str(Un))) + str(int(Un))

        if len(pname) == 0:
            pname = 'Unknown'

        doc = {
            'uid': uid,
            'pname': pname,
            'gps': gps,
            'description': description,
            'image': image,
            'gender': gend
        }


        add_patient_emergency(doc)

        nearest_hosp = get_nearest_hospital(gps)

        print(nearest_hosp)

        jsonData = {
            'status': 200,
            'message': 'successful! Help is on your way',
            'hosp_gps': nearest_hosp
        }
        self.write(json.dumps(jsonData))

    @coroutine
    def stats_feed(self):
        uid = self.get_argument('uid')
        pulse = self.get_argument('pulse')
        bp = self.get_argument('bp')
        oxygen = self.get_argument('oxygen')

    def write_error(self, status_code, message="Internal Server Error", **kwargs):
        jsonData = {
            'status': int(status_code),
            'message': message
        }
        self.write(json.dumps(jsonData))
