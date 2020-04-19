def beautifulBinaryString(b):
    monitor = []
    for i in b:
        monitor.append(i)

    counter = 0
    check = "010"

    for i in range(len(b)):
        if i > 2:
            temp = "".join(monitor[:i])
            if check == temp[i-3:i]:
                monitor[i-1] = "1"
                counter += 1

    if "".join(monitor).endswith(check):
        monitor[-1] = "1"
        counter += 1
    return counter


beautifulBinaryString("10110101101010")