import spacy 
import KeywordExtractor
import DefinitionExtraction
import ocr_on_text

nlp = spacy.load('en_core_web_sm'); 

def interpret_for_plain_text(file_path):
	try:
		with open(file_path, 'r') as file:
			content = file.read().replace('\n', '')

		keywords = KeywordExtractor.extractKeywordsFromContent(content)
		return keywords

	except FileNotFoundError:
		print("Couldn't find file.")

def interpret_for_ocr(img_path):
	try:
		content = ocr_on_text.get_text(img_path)
		keywords = KeywordExtractor.extractKeywordsFromContent(content)
		return keywords

	except FileNotFoundError:
		print("Couldn't find file.")

def write_keywords_to_file(keywords, file_name):
	keyword_file = open(file_name,"w")

	for word in keywords:
		keyword_file.write('%s\n' % word)

	keyword_file.close()


keywords = interpret_for_plain_text("psychtext.txt")
#keywords = interpret_for_ocr("historytest.png")
file_name = "keywords.txt"
write_keywords_to_file(keywords, file_name)

definitions = DefinitionExtraction.extract(file_name)

for p in definitions:
	print(p.word.upper())
	print('-'*150)
	for d in p.questions:
		print(d)
		print("\n")
