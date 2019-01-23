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
curl http://127.0.0.1:5000/doc2vec -X POST -H "Content-Type: application/json" --data '{"documents": ["私はペンを持っています", "私はサッカーが好きです", "彼はブロックチェーンに詳しです", "私はゲームが好きです"]}'
```

サンプル返り値

```

```
