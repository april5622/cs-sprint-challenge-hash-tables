def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    output = []
    d = {}

    # not enough from the inputs to give two indices
    if len(weights) == 1:
        return None 

    # make the weight as the value and the index as the key when adding weights to dictionary
    for i, weight in enumerate(weights):
        if i not in d:
            d[i] = weight

    # looping over dictionary to check if each pair would equal to the limit
    for k, v in d.items(): # one of the two indices
        for i, weight in d.items(): # one of the two indices
            if k != i: # if the two indices does not equal each other
                if length != 1: # if the length is not one
                    if v + weight == limit: # if the two value for the indices equals the limit
                        if k > i: # check for higher valued index to go first
                            output = [k, i]
                        else:
                            output = [i, k]
    return output
                


    # will return a tuple of integers that forms like (zero, one)