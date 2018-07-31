find object for web
====
WEB経由で画像をアップロードすることで物体の検出及び認識処理後の画像を返すアプリである.\
認識処理にはSingle Shot MultiBox Detector(SSD)[1]を用いている.

v 0.1.0 基本機能の完成.未検出の場合にエラーが発生する.

## Requirement
Chianer 4.x.x\
Chainercv 0.10.0\
numpy 1.14.0\
OpenCV 2.x.x\
Pillow 5.0.0\
django 1.11.0\

## Usage
* サーバーの起動 \
`$ python manage.py runserver`

* サーバーにアクセス\
ブラウザのURL欄に以下を入力してアクセス\
`http://127.0.0.1:8000/form/`

* 画像のアップロード\
認識対象の画像を選択し,送信をクリックする.\
しばらく経つとSSDによる認識処理を行い,入力画像と結果を描画した画像が表示される.

## Paper
[1] Lui, Wei et al. "SSD:SingleShot MultiBox Detector."arXiv preprint arXiv:1512.02325(2015).
