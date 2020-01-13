# [カードギャラリーから画像を取得してコレクター番号をファイル名にして保存]
#
# https://magic.wizards.com/ja/articles/archive/card-image-gallery/throne-eldraine
# 
# <div class="activecardblock"> 内に含まれる
# <img src="xxxx"> のxxxxにカード画像のURLが格納されている。
# これを順番にダウンロードし、連番をつけて保存すればよい。
#
# カードギャラリー内の画像はコレクター番号順に出現することを前提としており、
# サイト側がHTML構成を変えると本ツールは使えなくなる

import requests
from bs4 import BeautifulSoup

# ギャラリーからhtmlを取得
gallery_url = 'https://magic.wizards.com/ja/articles/archive/card-image-gallery/theros-beyond-death'
r = requests.get(gallery_url)
soup = BeautifulSoup(r.content, "html.parser")

# <div class="activecardblock"> のリストを取得
blocks = soup.find_all("div", class_="activecardblock")

# 以降、画像URL取得して画像ほ保存する処理
collecter_num = 1
for block in blocks:
    imgs = block.find_all("img")    # imgタグのリストを取得
    for img in imgs:
        file_url = img['src']       # 画像urlはsrc属性に格納されている

        # 画像URLを保存
        image = requests.get(file_url).content
        with open(str(collecter_num) + ".png", "wb") as f:
            f.write(image)

        # コレクター番号を更新
        collecter_num = collecter_num + 1
