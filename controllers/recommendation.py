import pickle

def get_all_recommendations(features):
    with open('internal/coll_filt/cf.pkl', 'rb') as f:
        kmeans = pickle.load(f)

    cluster = kmeans.evaluate(features)

    # find all users with cluster in database
    # return objects

get_all_recommendations([1,2,3])
