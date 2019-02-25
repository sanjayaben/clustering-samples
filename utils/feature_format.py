import numpy as np


def featureFormat( dictionary, features, exclude_features, remove_NaN=True, remove_all_zeroes=True, remove_any_zeroes=False):
    """ convert dictionary to numpy array of features
        remove_NaN = True will convert "NaN" string to 0.0
        remove_all_zeroes = True will omit any data points for which
            all the features you seek are 0.0
        remove_any_zeroes = True will omit any data points for which
            any of the features you seek are 0.0
        sort_keys = True sorts keys by alphabetical order. Setting the value as
            a string opens the corresponding pickle file with a preset key
            order (this is used for Python 3 compatibility, and sort_keys
            should be left as False for the course mini-projects).
    """


    return_list = []

    for val in dictionary:
        tmp_list = []
        for feature in features:
            if feature not in exclude_features:
                try:
                    val[feature]
                except KeyError:
                    print ("error: key ", feature, " not present")
                    return
                value = val[feature]
                if value=="NaN" and remove_NaN:
                    value = 0
                tmp_list.append( value )

        ### if all features are zero and you want to remove
        ### data points that are all zero, do that here
        if remove_all_zeroes:
            append = False
            for item in tmp_list:
                if item != 0 and item != "NaN":
                    append = True
                    break
        ### if any features for a given data point are zero
        ### and you want to remove data points with any zeroes,
        ### handle that here
        if remove_any_zeroes:
            if 0 in tmp_list or "NaN" in tmp_list:
                append = False
        ### Append the data point if flagged for addition.
        if append:
            return_list.append( np.array(tmp_list) )

    return np.array(return_list)
