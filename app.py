# -*- coding: utf-8 -*-

import os
import json

from flask import Flask, request, jsonify


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
        data = str(data['key'])

    # 結果を JSON にして返す
    return jsonify(
            {
                'result': data
            }
        )

if __name__ == '__main__':
    app.run()

