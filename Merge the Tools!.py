
#Consider the following:

#A string, , of length  where .
#An integer, , where  is a factor of .
#We can split  into  subsegments where each subsegment, , consists of a contiguous block of  characters in . Then, use each  to create string  such that:

#The characters in  are a subsequence of the characters in .
#Any repeat occurrence of a character is removed from the string such that each character in  occurs exactly once. In other words, if the character at some index  in  occurs at a previous index  in , then do not include the character in string .
#Given  and , print  lines where each line  denotes string .


string = input()
k = int(input())
def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    List = [x for x in string]
    div = int(n/k)
    minList = []

    for i in range(div):
        for j in range(k):
            minList.append(List[j])
        del(List[0:k])

        newList = []
        for y in minList:
            if y not in newList:
                newList.append(y)

        #print(f"newList = {newList}")
        for char in newList:
            print(f"{char}", end="")
        print()
        minList = []


merge_the_tools(string, k)