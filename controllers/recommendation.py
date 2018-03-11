# from controllers.modules import *
# from controllers.utility import *
#
# import pickle
# import env
# import asyncio
# import motor.motor_asyncio
#
#
#
# async def find_in_cluster(cluster):
#     coll = db['clustering_data']
#     cur = coll.find()
#
#     return await cur.to_list(10)
#
#
# def get_all_recommendations(features):
#     with open('../internal/coll_filt/cf.pkl', 'rb') as f:
#         kmeans = pickle.load(f)
#
#     cluster = kmeans.predict(features)
#     print(cluster)
#
#     loop = asyncio.get_event_loop()
#
#     return find_in_cluster(10)
#
# get_all_recommendations([[0, 1, 0, 0, 0, 1, 1, 1, 1, 1]])
#
# # test case - 0, 1, 0, 0, 0, 1, 1, 1, 1, 1 out - 0
