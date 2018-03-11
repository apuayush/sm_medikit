from controllers.modules import *
from controllers.utility import *


class EmergencyHandler(RequestHandler):
    def set_default_headers(self):
        print("setting headers!!!")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header('Access-Control-Allow-Methods', 'POST, OPTIONS')

    # emergency admissions
    def post(self):
        uid = self.get_argument('phone')
        pname = self.get_argument('name')
        gps = self.get_argument('gps')
        gend = self.get_argument('gender')
        description = self.get_argument('description')
        image = self.get_argument('image')

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
            'image': image
        }

        add_patient(doc)

        nearest_hosp = get_nearest_hospital(gps)
        # TODO - show closest hospital using maps api(Surya)

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
