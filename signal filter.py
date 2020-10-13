
#Sometimes it is necessary to filter a signal by frequency, e.g. to reduce noise outside of the expected frequency range.  Filters can be stacked, allowing only the frequencies within the range allowed by all filters to get through.  For example, three filters with ranges of (10, 17), (13, 15) and (13, 17) will only allow signals between 13 and 15 through.  The only range that all filters overlap is (13, 15).  Given n signals frequencies and a series of m filters that let through frequencies in the range x to y, inclusive, determine the number of signals that will get through the filters.

#For example, given n = 5 signals with frequencies = [8, 15, 14, 16, 21] and m = 3 filtersRanges = [[10, 17], [13, 15], [13, 17]], the 2 frequencies that will pass through all filters are 15 and 14.


def countSignals(frequencies, filterRanges):
    # Write your code here
    list_init, list_end, filter, result = [], [], [], []

    for list in filterRanges:
        list_init.append(list[0])
        list_end.append(list[1])
    filter.append(max(list_init))
    filter.append(min(list_end))

    for i in frequencies:
        if i >= filter[0] and i <= filter[1]:
            result.append(i)
    #print(filter)
    #print(result)
    #print(frequencies)
    #print(filterRanges)
    return len(result)


frequencies_count = int(input().strip())

frequencies = []

for _ in range(frequencies_count):
    frequencies_item = int(input().strip())
    frequencies.append(frequencies_item)

filterRanges_rows = int(input().strip())
filterRanges_columns = int(input().strip())

filterRanges = []

for _ in range(filterRanges_rows):
    filterRanges.append(list(map(int, input().rstrip().split())))

result = countSignals(frequencies, filterRanges)
print(f"result: {result}")