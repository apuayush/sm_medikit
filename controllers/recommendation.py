import asyncio
from controllers.modules import *
from controllers.utility import *


class RecommendationHandler(RequestHandler):
    def set_default_headers(self):
        print("setting headers!!!")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header('Access-Control-Allow-Methods', 'POST, OPTIONS')

    # emergency admissions

    def post(self):
        features = self.get_arguments('features')[0]
        features = features.replace(' ','').split(',')
        features = [int(i) for i in features]

        if type(features) == 'str':
            features = json.loads(features)

        cluster_match_list = get_all_recommendations([features])
        print(cluster_match_list)

        self.write(
            json.dumps({
                'match': cluster_match_list
            })
        )

    def write_error(self, status_code, message="Internal Server Error", **kwargs):
        jsonData = {
            'status': int(status_code),
            'message': message
        }
        self.write(json.dumps(jsonData))


async def find_in_cluster(cluster):
    coll = db1['clustering_data']
    cur = coll.find({'cluster': cluster}, {'_id':0})

    val = await cur.to_list(10)
    return val


def get_all_recommendations(features):
    with open('internal/coll_filt/cf.pickle', 'rb') as f:
        kmeans = pickle.load(f)

    cluster = kmeans.predict(features)
    print(cluster)

    loop = asyncio.get_event_loop()
    val = loop.run_until_complete(find_in_cluster(int(cluster[0])))

    return val
    # print(val)


# get_all_recommendations([[0, 1, 0, 0, 0, 1, 1, 1, 1, 1]])
#
# # test case - 0, 1, 0, 0, 0, 1, 1, 1, 1, 1 out - 0
