from flask import Flask, render_template, request
from text_summary import summarizer
from text_keyword import extract_keywords

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/textsummary', methods=['POST'])
def textsummary():
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        summary, original_txt, len_orig_txt, len_summary = summarizer(rawtext)
        return render_template('summary.html', summary=summary, original_txt=original_txt, len_orig_txt=len_orig_txt, len_summary=len_summary)

@app.route('/keywordextraction', methods=['POST'])
def keywordextraction():
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        keywords,doc,len_orig_txt,len_key = extract_keywords(rawtext)
        return render_template('textkeyword.html', original_txt=doc, keywords=keywords,len_orig_txt=len_orig_txt, len_key=len_key)

if __name__ == "__main__":
    app.run(debug=True)
