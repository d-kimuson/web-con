# Web Con

## 依存関係

このプロジェクトでは、

- [Python](https://www.python.jp/)
- [pipenv](https://pipenv-ja.readthedocs.io/ja/translate-ja/)
- [Node.js](https://nodejs.org/ja/)
- [Yarn](https://classic.yarnpkg.com/ja/)

を使いますので、インストールされてない場合は取得してください

pipenv については、以下の環境変数が設定されていることを確認してください

``` bash
export PIPENV_VENV_IN_PROJECT=1
export PIPENV_IGNORE_VIRTUALENVS=1
```

## 環境構築

以下のスクリプトで初期設定をします

``` bash
$ ./bin/setup.sh
```

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

## VSCodeの設定

`extensions.json` に推奨パッケージが書かれているのでインストールします

`.vscode/settings.json` の `mypy.executable` を自分の環境のものに差し替えます

``` json
{
  "mypy.executable": "/path/to/web_con/.venv/bin/mypyls",  // <= ここ
  "mypy.configFile": "./backend/mypy.ini",
  "mypy.targets": [
    "./backend"
  ],
}
```
