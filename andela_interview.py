
#print out compound words from the list of given words

all_words = ['cat', 'basket', 'shipping', 'walk', 'amateur', 'am', 'rate', 'international', 'mouth', 'flat', 'little']
given = ['catwalk', 'shippingrate', 'international', 'basketmouth', 'walking', 'amateur', 'walkamateur', 'flatrate', 'xml', 'amlittle']

def comp():
	#time complexity of O(n*2)
	compound_words = []
	for word in given:
		for lword in all_words:
			if word.startswith(lword):
				mod_word = word[len(lword)-1:]
				for rword in all_words:
					if mod_word.endswith(rword):
						compound_words.append(word)
	return compound_words

def compound():
	#time complexity of O(n*2)
	compound_words = []
	count = 0
	for word in given:
		for dictWord in all_words:
			if dictWord in word:
				count += 1
		if count > 1:
			compound_words.append(word)
		count = 0
	return compound_words

def compound2():
	#time complexity of O(n)
	global all_words
	global given
	all_words = set(all_words)
	given = set([word for word in given if word not in all_words])
	compound_words = [word for word in given for dict_word in all_words if word.startswith(dict_word) and len(word[len(dict_word):])]
	compound_words = [word for word in compound_words for dict_word in all_words if word.endswith(dict_word) and len(word[:len(dict_word)-1])]
	return compound_words

print(compound2())
