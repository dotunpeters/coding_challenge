def formingMagicSquare(s):
    """
        ##########Pseudocode##########
        empty_dict = {}
        notFound = []
        excess = []
        sqr = math.sqrt(len(s))
        for i in range(sqr):
            for j in range(sqr):
                counter = s[i].count(s[i][j])
                if s[i][j] in empty_dict:
                    empty_dict[s[i][j]] += counter
                else:
                    empty_dict[s[i][j]]

        for i in range(1, len(s)):
            if i not in empty_dict:
                notFound.append(i)

        for i in empty_dict:
            if empty_dict[i] > 1:
                for j in range(empty_dict[i] - 1):
                    excess.append(empty_dict[i])

        sum = 0
        for i in range(len(excess)):
            sub = math.abs(notFound[i] - excess[i])
            sum += sub
        
        return sum
    """

    empty_dict = {}
    notFound = []
    excess = []
    lenght = 1
    for i in range(len(s)):
        for j in range(len(s[i])):
            lenght += 1
            counter = s[i].count(s[i][j])
            print(s[i][j], counter)
            if s[i][j] in empty_dict and s[i].count(s[i][j]) == 1:
                empty_dict[s[i][j]] += counter
            else:
                empty_dict[s[i][j]] = counter

    for i in range(1, lenght):
        if i not in empty_dict:
            notFound.append(i)

    for i in empty_dict:
        if empty_dict[i] > 1:
            for j in range(empty_dict[i] - 1):
                excess.append(i)

    sum = 0
    print(empty_dict)
    print(notFound)
    print(excess)
    for i in range(len(excess)):
        sub = abs(notFound[i] - excess[i])
        sum += sub
    
    return sum

