```
$ ./start.sh ABC123
```

を実行すると、ABC123というディレクトリが生成され、その中に問題ごとの.pyファイルが生成される。

## コードテスト
```
$ python3 make_sample.py > sample.txt
$ python3 ABC123/A.py < sample.txt
```

## 実行時間測定
```
$ time python3 ABC123/A.py < sample.txt
```
