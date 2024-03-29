# -*- coding: utf-8 -*-

import os
import json
from os import path

from flask import Flask, request, jsonify
from janome.tokenizer import Tokenizer
from gensim.models.doc2vec import Doc2Vec
from gensim.models.doc2vec import TaggedDocument


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


def words(doc):
    t = Tokenizer()
    return [token.surface for token in t.tokenize(doc) if token.part_of_speech.split(',')[0] in ['名詞']]


@app.route('/')
def index():
    return 'Hello World!'

@app.route('/doc2vec', methods=['POST'])
def doc2vec():
    if request.method == 'POST':
        data = request.data.decode('utf-8')
        data = json.loads(data)
        documents = data['documents']

    tags = [f'doc{i+1}' for i in range(0, len(documents))]
    train_docs = [TaggedDocument(words=words(document), tags=[tag]) for document, tag in zip(documents, tags)]
    model = Doc2Vec(documents=train_docs, min_count=1, dm=0)

    result = {tag: {"document": document, "distances": model.docvecs.most_similar(tag)} for document, tag in zip(documents, tags)}

    # 結果を JSON にして返す
    return jsonify(
            {
                'result': result
            }
        )

if __name__ == '__main__':
    app.run()

