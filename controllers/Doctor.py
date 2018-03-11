from controllers.modules import *
from controllers.utility import *
import asyncio


class LoginHandler(RequestHandler):
    def set_default_headers(self):
        print("setting headers!!!")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header('Access-Control-Allow-Methods', 'POST, OPTIONS')


    async def post(self):
        # uid = self.get_argument('uid')
        # password = self.get_argument('password')

        data = json.loads(self.request.body.decode('utf-8'))
        uid = data['uid']
        password = data['password']

        print(password)

        docs = db.collection('doctor').where('username', '==', uid).get()
        if docs is None:
            self.write(json.dumps(dict(
                status="403",
                message="Doctor not registered"
            )
            ))

        doctor = list(docs)[0].to_dict()
        print(doctor)
        pswd = doctor['password']

        if password == pswd:
            self.write(json.dumps(dict(
                status="200",
                message="registration successful",
                doc_id=doctor['id'],
                doc_name=doctor['username']
            )
            ))

        else:
            self.write(json.dumps(dict(
                status="403",
                message="invalid password"
            )
            ))

    def write_error(self, status_code, message="Internal Server Error", **kwargs):
        jsonData = {
            'status': int(status_code),
            'message': message
        }
        self.write(json.dumps(jsonData))

    def options(self):
        self.set_status(204)
        self.finish()


class LogoutHandler(RequestHandler):
    """
    method = POST
    route : /logout
    parameter : token
    """
    def set_default_headers(self):
        print("setting headers!!!")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "*")
        self.set_header('Access-Control-Allow-Methods', ' POST, OPTIONS')

    @coroutine
    def post(self):
        token = self.get_argument("token")

        db1.token.remove({"token": token})
        self.write({"status": 200, "msg": "successful"})

    def options(self):
        self.set_status(204)
