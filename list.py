
#if __name__ == '__main__':
#    N = int(input())
#    list = []
#    commands = []
#    for _ in range(N):
#        commands.append(input())
#    for each_command in commands:
#        each = each_command.split(" ")
#        if each[0] == "print":
#            print(list)
#        elif each[0] == "insert":
#            list.insert(int(each[1]), int(each[2]))
#        elif each[0] == "remove":
#            list.remove(int(each[1]))
#        elif each[0] == "append":
#            list.append(int(each[1]))
#        elif each[0] == "reverse":
#            list.reverse()
#        elif each[0] == "pop":
#            list.pop()
#        elif each[0] == "sort":
#            list.sort()



if __name__ == '__main__':
    n = int(input())
    tup = input().split(" ")
    integer_list = tuple((int(tup[0]), int(tup[1])))
    print(hash(integer_list))
