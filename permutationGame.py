def permutationGame(arr):
    #
    # Write your code here.
    #
    player = 0
    while True:

        if len(arr) == 1:
            if player%2 == 0:
                return "Bob"
            else:
                return "Alice"

        if arr == sorted(arr):
            if player%2 == 0:
                return "Bob"
            else:
                return "Alice"
            
        maxim = arr.index(max(arr))
        arr.pop(maxim)
        player += 1

print(permutationGame([11, 9, 10, 5, 8, 3, 2, 7, 6, 4, 1]))
print(permutationGame([10, 7, 9, 2, 5, 8, 4, 1, 3, 6]))
print(permutationGame([3, 4, 5, 1, 2]))
print(permutationGame([15, 2, 4, 10, 12, 13, 8, 7, 11, 14, 1, 6, 5, 9, 3]))
print(permutationGame([9, 4, 7, 10, 13, 12, 8, 6, 2, 5, 1, 14, 3, 15, 11]))