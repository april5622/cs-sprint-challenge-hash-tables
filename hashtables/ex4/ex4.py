def has_negatives(a):
    """
    YOUR CODE HERE
    """
    d = {}
    result = []
    a.sort(reverse=True) # sorting the list in descending order

    # make all index as keys and value as value when adding integers to the dict
    for i, v in enumerate(a):
        d[v] = i
    
    # looping through the dictionary and if key is greater than 0,
    for k, v in d.items():
        if k > 0:
            # this will check if any of the keys are negative integers
            cur = (k -(k*2))
            # if they are not they will be added into the list
            if d.get(cur):
                result.append(k)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
