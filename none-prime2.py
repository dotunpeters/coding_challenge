def main():
    def manipulate_generator(generator, n):

        # Prime Function return 1 if the argument is prime
        # it return 0 if the argument is none-prime
        def prime(i):
            for x in range(2, i):
                if i%x == 0:
                    return 0
                else:
                    continue
            return 1
        
        # initialize variable count
        # initialize generator_list using list comprehension
        count = 0
        genList = [m+1 for m in range(n*2)]

        # iterate through genList to print the require none-prime
        # numbers in n number of times
        for j in genList:
            if n == 1:
                print(n)
                break
            if prime(j) == 0:
                count += 1
                if count == n-1:
                    print(j)
                    break


    def positive_integers_generator():
        n = 1
        while True:
            x = yield n
            if x is not None:
                n = x
            else:
                n += 1

    k = int(input())
    g = positive_integers_generator()
    for _ in range(k):
        n = next(g)
        manipulate_generator(g, n)


if __name__ == "__main__":
    main()