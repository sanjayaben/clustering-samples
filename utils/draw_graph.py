import matplotlib.pyplot as plt

def draw_cluster(pred, features, centers, f1_name, f2_name):
    """ some plotting code designed to help you visualize your clusters """
    colors = ['b', 'g', 'c', 'm', 'y', 'k', 'w']
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])
    for center in centers:
        plt.scatter(center[0],center[1],color="r", marker="X", s=100.0)
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.show()