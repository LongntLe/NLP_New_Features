from nltk.parse.stanford import StanfordDependencyParser
import os

#set-up
java_path = r"path\to\java"
os.environ["JAVAHOME"] = java_path

#load_model
path_to_jar = r"path\to\stanford-parser.jar"
path_to_models_jar = r"path\to\stanford-parser-3.8.0-models.jar"
stanford_parser = StanfordDependencyParser(path_to_jar=path_to_jar, 
	path_to_models_jar=path_to_models_jar, encoding="utf-8")

def parser(sent_list): #input: list of sentences
	"""
    This function takes a list of sentences and detect whether each sentence is written in passive or active voice.
    This function only notifies for a fix if the sentence is passive. 
    """
    text = stanford_parser.raw_parse_sents(sent_list)
    #Extract feature from the Dependency Graph. Documentation: http://www.nltk.org/_modules/nltk/parse/dependencygraph.html
    for f in list(text):
        for w1, rel, w2 in next(f).triples():
            if rel == "nsubjpass":
                print(w2[0], w1[0])