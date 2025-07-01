import sys

def get_book_text():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
	else:
		path_to_book = sys.argv[1]
		with open(path_to_book, "r") as f:
			book_text = f.read()
		return book_text, path_to_book

def num_words(text):
	words = text.split()
	return len(words)

def char_count(text):
	char_count = []
	chars_list = set(text.lower())
	for char in chars_list:
		if char.isalpha() != True:
			pass
		else:
			lower = text.lower()
			count = lower.count(char)
			chars = {"char":char, "count":count}
			char_count.append(chars)
	#		print(char, count) #testing
	return char_count
	
def sort_on(items):
	return items["count"]

def make_report(path_to_book):
	text, path = get_book_text()
	word_count = num_words(text)
	character_count = char_count(text)
#	print(character_count) #testing
	character_count.sort(reverse=True, key=sort_on)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {path_to_book}...")
	print("----------- Word Count ----------")
	print(f"Found {word_count} total words")
	print("--------- Character Count -------")
#	print(character_count) #testing
	for pair in character_count:
#		print(pair)
		values = list(pair.values())
#		print(values) #testing
		print(values[0] + ": " + str(values[1]))
	print("============= END ===============")
