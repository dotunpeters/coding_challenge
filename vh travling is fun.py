
def connectedCities(n, threshold, originCities, destinationCities):
    # Write your code here
    result = []

    #Function returns path existence
    def gcd(x, y, threshold):
        x_gcd = []
        y_gcd = []

        #append each divisor of x to x_gcd
        for i in range(x):
            i += 1
            if x%i == 0:
                x_gcd.append(i)

        #append each divisor of y to y_gcd
        for i in range(y):
            i += 1
            if y%i == 0:
                y_gcd.append(i)


        x_gcd = [x for x in x_gcd if x > threshold]
        y_gcd = [y for y in y_gcd if y > threshold]
        if len(x_gcd) == 0 or len(y_gcd) == 0:
            return 0
        else:
            return 1

    #Iterate and check if Greatest Common Divisor exist to append the
    #corresponding return to the result list
    n = len(originCities)
    for i in range(n):
        if gcd(originCities[i], destinationCities[i], threshold) == 1:
            result.append(1)
        else:
            result.append(0)
    return result


if __name__ == '__main__':

    n = int(input().strip())

    g = int(input().strip())

    originCities_count = int(input().strip())

    originCities = []

    for _ in range(originCities_count):
        originCities_item = int(input().strip())
        originCities.append(originCities_item)

    destinationCities_count = int(input().strip())

    destinationCities = []

    for _ in range(destinationCities_count):
        destinationCities_item = int(input().strip())
        destinationCities.append(destinationCities_item)

    result = connectedCities(n, g, originCities, destinationCities)
    print(f"result: {result}")