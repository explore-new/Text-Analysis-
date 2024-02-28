import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

def summarizer(rawdocs):
    # Load English language model and stop words
    stopwords = list(STOP_WORDS)
    nlp = spacy.load('en_core_web_sm')

    # Tokenize the document
    doc = nlp(rawdocs)

    # Calculate word frequency
    word_freq = {}
    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text] = 1
            else:
                word_freq[word.text] += 1

    # Normalize word frequencies
    max_freq = max(word_freq.values())
    for word in word_freq.keys():
        word_freq[word] = word_freq[word] / max_freq

    # Tokenize sentences
    sent_tokens = [sent for sent in doc.sents]

    # Calculate sentence scores based on word frequencies
    sent_scores = {}
    for sent in sent_tokens:
        for word in sent:
            if word.text in word_freq.keys():
                if sent not in sent_scores.keys():
                    sent_scores[sent] = word_freq[word.text]
                else:
                    sent_scores[sent] += word_freq[word.text]

    # Select a percentage of top-scoring sentences
    select_len = int(len(sent_tokens) * 0.3)
    
    # Use nlargest to get the top sentences based on scores
    summary = nlargest(select_len, sent_scores, key=sent_scores.get)

    # Convert the selected sentences into the final summary
    final_summary = [sent.text for sent in summary]
    summary = ' '.join(final_summary)

    # Return the summary, original document, word count, and summary word count
    return summary, doc, len(rawdocs.split(' ')), len(summary.split(' '))

'''import spacy 
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation 
from heapq import nlargest
def summarizer(rawdocs): 
			stopwords=list(STOP_WORDS)
			#print(stopwords)
			nlp=spacy.load('en_core_web_sm')
			doc=nlp(rawdocs)
			#print(doc) #print the whole text
			token= [token.text for token in doc]
			#print(token) #print the list of all the words in the text
			word_freq={}
			for word in doc:
				if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
					if word.text not in word_freq.keys():
						word_freq[word.text]=1
					else:
						word_freq[word.text]+=1
			#print(word_freq)  #print the frequency of each word
			max_freq=max(word_freq.values())
			#print(max_freq)  #print the maximum frequency of the word
			for word in word_freq.keys():
				word_freq[word]=word_freq[word]/max_freq
			#print(word_freq)  #print the tuple of avg freqency of each words
			sent_tokens=[sent for sent in doc.sents]
			#print(sent_tokens)  #print the sentence list
			sent_scores={}
			for sent in sent_tokens:
				for word in sent:
					if word.text in word_freq.keys():
						if word.text in word_freq.keys():
							sent_scores[sent]=word_freq[word.text]
						else:
							sent_scores[sent]+=word_freq[word.text]
			#print(sent_scores)  #print the score of each sentence
			select_len=int(len(sent_tokens)*0.3)
			print(select_len)
			summary= nlargest(select_len, sent_scores, key=sent_scores.get)
			#print(summary)
			final_summary=[word.text for word in summary]
			summary= ' '.join(final_summary)
			#print(text)
			#print(summary)
			#print("length of original text ",len(text.split(' ')))
			#print("length of summary text ",len(summary.split(' ')))
			return summary,doc,len(rawdocs.split(' ')),len(summary.split(' '))'''
