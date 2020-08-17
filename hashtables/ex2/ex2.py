#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    dict = {}
    
    # adding all tickets to a dict and the source is in the key and destination is value
    for i in tickets:
        dict[i.source] = i.destination

    start = dict['NONE']
    route = [start]
    count = 0

    # looping through the dictionary
    for _ in dict:
        for s, d in dict.items():
            if count > 0:
                if start == s and d != 'NONE':
                    # a route will be added to the dict when the destination equals the source of the next
                    route.append(d)
                    start = dict[s]
            count += 1
    route.append('NONE') # appending to NONE the source of the first route
    
    return route
