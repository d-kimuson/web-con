# Web Con

## 開発を始める

``` bash
$ ./setup.sh
```

`.bashrc` に

``` bash
export PIPENV_VENV_IN_PROJECT=1
export PIPENV_IGNORE_VIRTUALENVS=1
```

を書いてください

## 開発サーバーを建てる

フロントとバックのサーバーをそれぞれ建てます

``` bash
$ cd backend
$ pipenv run start
```

``` bash
$ cd frontend
$ yarn dev
```
