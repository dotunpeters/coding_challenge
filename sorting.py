
listing = [['Dotun', 'peter', 10, 'M'], ['Sola', 'paul', 4, 'M'], ['Kunle', 'Johnson', 2, 'M'], ['Pascal', 'stella', 9, 'M']]
print(listing)
listing.sort(key=lambda n:n[2])
print(listing)