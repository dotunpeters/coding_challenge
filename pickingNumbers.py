
def pickingNumbers(a):
    # Write your code here
    """"
        ###########Pseudocode############
        sort a
        counter
        sort list set(a)
        -> for val in list:
            -> if next value:
                -> if next val - val <= 1:
                    -> count val and next val in a
                    -> append to counter

        return max(counter)
    """

    a.sort()
    counter = []
    unique = sorted(list(set(a)))
    
    if len(unique) == 1:
        return len(a)

    for i in range(len(unique)):
        try:
            if unique[i+1]:
                if unique[i+1] - unique[i] <= 1:
                    count = a.count(unique[i]) + a.count(unique[i+1])
                    counter.append(count)

                count = a.count(unique[i])
                counter.append(count)
        except:
            break

    return max(counter)
            
