import spacy

def get_all_verbs(rawdocs):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(rawdocs)
    return {token.lemma_.lower() for token in doc if token.pos_ == 'VERB'}

def extract_keywords(rawdocs):
    nlp = spacy.load("en_core_web_sm")
    
    doc = nlp(rawdocs)
    # Get verbs to exclude using the get_all_verbs function
    verbs_to_exclude = get_all_verbs(rawdocs)

    # Customize stop words to include common abbreviations
    stop_words = nlp.Defaults.stop_words.union({'etc', 'e.g', 'i.e','word','able','essential','long'})

    # Process the text using spaCy
    doc = nlp(rawdocs)

    # Extract individual words (lemmas) as keywords, excluding specified verbs and stop words
    keywords = list(set([token.lemma_ for token in doc if token.is_alpha and not token.is_stop and token.lemma_.lower() not in verbs_to_exclude and token.lemma_.lower() not in stop_words]))

    return keywords,doc,len(rawdocs.split(' ')),len(keywords)

