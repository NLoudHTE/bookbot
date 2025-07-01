#def get_book_text(path_to_book):
#    with open(path_to_book) as f:
#        file_contents = f.read()
#        return file_contents
from stats import get_book_text
from stats import num_words
from stats import char_count
from stats import make_report
from stats import sort_on

def main():
#	text = get_book_text()
#	tally = num_words(text)
#	character_count = char_count(text)
	text, path_to_book = get_book_text()
	make_report(path_to_book)

main()
