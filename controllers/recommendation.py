import pickle
import motor

client = motor.motor_asyncio.AsyncIOMotorClient()
db = client.sm_medikit

async def find_in_cluster(cluster):
    coll = db['clustering_data']
    cur = coll.find()
    from pprint import  pprint
    for doc in await cur.to_list():
        pprint(doc)


def get_all_recommendations(features):
    with open('internal/coll_filt/cf.pkl', 'rb') as f:
        kmeans = pickle.load(f)

    cluster = kmeans.evaluate(features)


    # return objects

find_in_cluster(2)
