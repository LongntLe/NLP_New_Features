from enchant.checker import SpellChecker
from nltk.tag import SennaNERTagger
def spell_checker(l):
	ner = SennaNERTagger(r"path_to_senna")
	chkr = SpellChecker("en_US")
	chkr.set_text(l)
	for err in chkr:
		#print(err.word)
		if ner.tag(err.word.split())[0][1] == "O":
			print(err.word)
			print("Did you mean: ", err.suggest()[0])