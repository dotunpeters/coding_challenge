
def pageCount(n, p):
    #
    # Write your code here.
    #
    """
        ###########Pseudocode###########
        -> n = number of pages
        -> p = target page

        -> if p is close to first page:
            -> return int(p/2)
        -> if p is close to the last page:
            -> return int(p/2)
    """
    middle = int(n/2)
    diff = n-p
    if p <= middle:
        return int(p/2)
    else:
        if (n%2 == 0 and diff == 0) or (n%2 != 0 and diff < 2):
            return 0
        elif n%2 == 0 and diff == 1 or (n%2 != 0 and diff < 5):
            return 1
        else:
            return int((diff)/2)

print(pageCount(18183, 18042))