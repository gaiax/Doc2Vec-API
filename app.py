# -*- coding: utf-8 -*-

import os
import json
from os import path

from flask import Flask, request, jsonify
from gensim.models.doc2vec import Doc2Vec
from gensim.models.doc2vec import TaggedDocument


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


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
    train_docs = [TaggedDocument(words=words, tags=[tag]) for words, tag in zip(documents, tags)]
    model = Doc2Vec(documents=train_docs, min_count=1, dm=0)

    result = {tag: model.docvecs.most_similar(tag) for tag in tags}

    # 結果を JSON にして返す
    return jsonify(
            {
                'result': result
            }
        )

if __name__ == '__main__':
    app.run()

