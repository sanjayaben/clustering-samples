import pickle
from sklearn.cluster import KMeans

from utils.draw_graph import draw_cluster
from utils.feature_format import featureFormat

student_list = pickle.load( open( "student_data_cluster.pkl", "rb" ))
print( '\n'.join('{}: {}'.format(*k) for k in enumerate(student_list)))

feature_list = ["past_perf","eng_level","stu_interest","sp_needs"]
exclude_features = ["stu_name"]
data = featureFormat(student_list,feature_list,exclude_features)

kmeans = KMeans(n_clusters=3, random_state=0).fit(data)
groups = kmeans.labels_
centers = kmeans.cluster_centers_
print("Group list: ", groups)
print("Cluster Centers", centers)

for i,student in enumerate(student_list):
    print(student["stu_name"], " :: ", groups[i])

draw_cluster(groups,data,centers,feature_list[0],feature_list[1])


