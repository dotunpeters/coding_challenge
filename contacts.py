
#!/bin/python3

import os
import sys

#
# Complete the contacts function below.
#
def contacts(queries):
    #
    # Write your code here.
    #
    #return queries
    listings = []
    result = []
    count = 0
    for each in queries:
        if each[0] == "add":
            listings.append(each[1])
        if each[0] == "find":
            for value in listings:
                if each[1] in value:
                    count += 1
            result.append(count)
            count = 0
    return result


if __name__ == '__main__':

    queries_rows = int(input())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    print(result)
