# fieldpoly-json

筆ポリゴンの.shpファイルをgeojson形式に変換するスクリプトです。

要求：

1. Ubuntu  18.04+

2. ```apt install ogre-1.9-tools```


つかいかた：

1. [農水省HP](https://www.maff.go.jp/j/tokei/porigon/)より筆ポリゴンをダウンロード

2. ```unzip -O sjis [都道府県名.zip]```


3. ```git clone https://github.com/kazulagi/fieldpoly-json.git```


4. ```python3 fieldpoly-json/GetGeoJson.py [都道府県名]```

バグ：
jsonの中身が一部文字化けします。どうしましょ。