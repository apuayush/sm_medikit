from controllers.modules import *
from controllers.utility import *


class PatientHandler(RequestHandler):
    def set_default_headers(self):
        print("setting headers!!!")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header('Access-Control-Allow-Methods', 'POST, OPTIONS')

    @coroutine
    def post(self):
        uid = self.get_argument('uid')
        pname = self.get_argument('name')
        gps = self.get_argument('gps')

        gend = self.get_argument('gender')
        description = self.get_argument('description')

        # image = self.get_argument('image')

        if len(uid) == 0:
            Un += 1
            uid = '0' * (12-len(str(Un))) + str(int(Un))
        if len(pname) == 0:
            pname = 'Unknown'

        fb.post('/livePatient', {'uid':uid, 'pname': pname, 'gps': gps, 'description': description})

        res = fb.get('/history',int(uid))

        if res == None:
            res = dict()
            res[int(uid)] = {'pname': pname, 'history':[], 'gender': gend}

        res[int(uid)]['history'].append({'date':time.strftime("%Y-%m-%d %H:%M"), 'description':description,'gps': gps })
        fb.post('/history',res)

        jsonData = {
            'status': 200,
            'message': 'successful! Help is on your way'
        }
        self.write(json.dumps(jsonData))

    def write_error(self, status_code, message="Internal Server Error", **kwargs):
        jsonData = {
            'status': int(status_code),
            'message': message
        }
        self.write(json.dumps(jsonData))
