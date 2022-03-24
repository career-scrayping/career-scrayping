# career-scrayping
インターン情報のスクレイピングをします。

## dokcerの操作方法
最初
```
$ docker-compose up --build
```

build以降
```
$ docker-compose up -d
```
バックグラウンドでdockerを動かすことができる
これでポート5000にアクセスすればok

```
$ docker-compose ps
```
コンテナの状況をみることができる

```
$ docker container exec -it web-scrayping bash
```
これでコンテナの中に入ることができる
