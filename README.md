# Doc2Vec-API
文章を複数投げたらdoc2vecを用いて文章同士の類似度を計算して返すAPIです

# 使い方
以下の形式のJSONをPOSTするだけです

```json
{
  "documents": ["文章1", "文章2", ・・・]
}
```

サンプル

```
curl  https://doc2vec-api.herokuapp.com/doc2vec -X POST -H "Content-Type: application/json" --data '{"documents": ["私はペンを持っています", "私はサッカーが好きです", "彼はブロックチェーンに詳しです", "私はゲームが好きです"]}'
```

サンプル返り値

```
{
  "result":{
    "doc1":{
      "distances":[
        ["doc4",0.25012192130088806],
        ["doc3",0.10284949839115143],
        ["doc2",0.07779199630022049]
      ],
      "document":"私はペンを持っています"
    },
    "doc2":{
      "distances":[
        ["doc1",0.07779199630022049],
        ["doc3",-0.02104666829109192],
        ["doc4",-0.046385545283555984]
      ],
      "document":"私はサッカーが好きです"
    },
    "doc3":{
      "distances":[
        ["doc1",0.10284949839115143],
        ["doc4",0.0043702274560928345],
        ["doc2",-0.021046670153737068]
      ],
      "document":"彼はブロックチェーンに詳しいです"
    },
    "doc4":{
      "distances":[
        ["doc1",0.25012192130088806],
        ["doc3",0.0043702274560928345],
        ["doc2",-0.046385545283555984]
      ],
      "document":"私はゲームが好きです"
    }
  }
}
```

# ローカル環境
```
# pipenvでパッケージインストール&仮想環境構築
$ pipenv install
# flaskの起動
$ pipenv run python3 app.py
```
