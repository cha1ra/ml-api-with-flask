# coding: utf-8
from flask import Flask, jsonify
from sklearn.externals import joblib

app = Flask(__name__)

# モデルはグローバル変数で読み込む
model = joblib.load('model.pkl')


@app.route('/')
def hello():
    # 推論の処理
    result = {'y': 10}
    return jsonify(result)


if __name__ == '__main__':
    app.run()
