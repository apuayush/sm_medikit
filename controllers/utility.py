from controllers.modules import *


def setToken(user, name):
    """
    setting tokens and saving them on database
    :param user:
    :return:
    """
    now = datetime.now()
    time = now.strftime("%d-%m-%Y %I:%M %p")
    token = jwt.encode({"uid": user, "time": time},
                       JWT_SECRET, JWT_ALGORITHM)

    db.token.insert({"token": token.decode(), "uid": user, "uname": name})

    return token.decode()


def aadhar_scanner_parser(xml_data):

    data = xmltodict.parse(xml_data)
    data = dict(data['PrintLetterBarcodeData'])
    return {'uid':data['@uid'],'uname':data['@name']}


def hash(data):
    data_hash = sha256(json.dumps(data, sort_keys=True).encode('utf-8')).hexdigest()
    return data_hash


def validate(tid):
    flag = 1
    lst = []
    while(tid!=""):
        try:
            cur = db.transactions.find({"transaction_id": tid})[0]
        except IndexError:
            flag = 0
            break
        last = cur['previous_transaction']
        #print "tid : ", tid
        #print "last : ", last
        #print "cur : ", cur['transaction_id']
        data = dumps({"from_id": cur['from_id'], "to_id": cur['to_id'],\
            "transaction_id": cur['last_item_transaction'], "last_transaction": cur['previous_transaction']})
        val = hash(data)
        if val!=tid:
            flag = 0
            break
        tid = last
    return str(flag)

