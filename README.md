# software_presentation
## 環境の作り方
### 1. 事前準備

```Shell
$ git clone https://github.com/itokaoru/software_presentation.git
```
Docker イメージを作成する.


```Shell
$ make build run
```

アプリを立ち上げる
```Shell
$ cd softproject
$ python manage.py runserver 172.17.0.2:8000
```
IPアドレスは
```Shell
$ docker container ls
```
でCONTAINER ID をコピーし,
```Shell
$ docker inspect CONTAINER ID
```
でNetworksという項目のIPAdressを使う.

一度イメージを作ってしまえば以降,
```Shell
$ make run
```
抜けるときは
```Shell
$ exit
```
