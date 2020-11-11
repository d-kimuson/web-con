# Web Con

とりあえず、ドキュメントを用意するほどの規模でもないのでここに共有したい内容を書き起こしておきます

規模感が大きくなって必要性に駆られたら、なんらかのドキュメントサーバーやサービスに置き換えを検討しましょう

## 準備

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

また、エディタ等は任意ですが、

[VSCode](https://code.visualstudio.com/) のエディタ設定やプラグイン設定、デバッグ構成等を共有しているので、こちらを推奨します

## 環境構築

以下のスクリプトで初期設定をします

``` bash
$ ./bin/setup.sh
```

流れは追ってもらえれば良いと思いますが、

- `git hooks` の設定
- データベースコンテナの構築 & 起動
- マイグレーションの適用
- パッケージのインストール
- 環境変数用の `.env` ファイルの準備

をしています

`.env` については `.env.example` をコピーしてるだけなので、必要時応じて上書きしてください

### VSCodeの設定

`VSCode` を使わない場合は読み飛ばし推奨です

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

## 開発サーバーを建てる

開発時は、フロント(`webpack`)とバック(`Django`)のサーバーをそれぞれ建てる必要があります

<details>
<summary>役割</summary>

`Django` サーバーでは、通常のDjango用開発サーバーです

`Django` 開発サーバーは、フロント周り(`html`, `css`, `js`)のホットリロードやプリプロセッサ(`sass`, `postcss`, `TypeScript` 等)対応が弱いので、`webpack` 開発サーバーで補助しています
</details>

``` bash
$ cd backend
$ pipenv run start
```

``` bash
$ cd frontend
$ yarn dev
```

これで、

- `Django` : http://localhost:8000
- `webpack`: http://localhost:3000

に開発サーバーが立ち上がります

基本的には、`webpack` の http://localhost:3000 を使ってください

`Django` サーバーから配信されるリソースについてもプロキシを通じて `webpack` サーバーからアクセスできます

## データベースサーバーの起動

開発環境用のデータベースとして、`MySQL` の Dockerコンテナを使います

``` bash
$ ./bin/start_db.sh
# または
$ cd backend/db && make start
```

で起動します

他にもいくつかコマンド(`stop`, `restart`, `connect`, ...etc) が用意されていますので、`Makefile` を確認してください

※ **データの永続化はしてません**

コンテナを破棄するとデータも消えます。

共有しておきたいデータについては

``` bash
$ pipenv run dump_db
```

をすると、`json` 形式で現在のデータベース情報が書き出されますので、こちらから必要なものを `fixtures/dev_min.json` に書いてコミットに含めてください

## リモートブランチ運用ルール

現時点(2020/11)では、

- 開発者が2人しかいない
- またMVPすら完成していない

ことから、簡易的な [Github Flow](https://guides.github.com/introduction/flow/) を用います

`Github Flow` では、`master` にデプロイ可能なコードを置いてあることを保証し、そのためにトピックブランチ(`feature/*`)からのプルリクエストを通じて、CIやレビューのフローを踏みますが、このプロジェクトではまだ本番環境や本番環境向けのCI環境が整っていません

そのため、現時点では `master` に直接コミットすることを推奨します

レビューが欲しい場合(いわゆる `WIP` プルリクを送りたいとき)等は好きにリモートブランチを使ってください

この辺のルールは、ある程度ソフトウェアが完成して、本番環境周りの環境が構築できた後にまた更新しようと思います

※ あくまでリモートブランチのルールなので、当然ローカルのブランチは好きに使ってください

## プロジェクト管理

[Github Project](https://github.com/d-kimuson/web-con/projects/1) でタスク管理をします

Issueを作成してプロジェクトに割り当てるとこのボードに追加されます

各自で自分のタスクを管理するために使ってください

## 静的解析と自動整形と Git フックス

このプロジェクトでは、[Git フック](https://git-scm.com/book/ja/v2/Git-%E3%81%AE%E3%82%AB%E3%82%B9%E3%82%BF%E3%83%9E%E3%82%A4%E3%82%BA-Git-%E3%83%95%E3%83%83%E3%82%AF) を利用して、コミット前にコード整形と静的解析を挟んでいます

フォーマッタ及び静的解析ツールとして、

- [mypy](https://github.com/python/mypy)
- [flake8](https://pypi.org/project/flake8/)
- [autopep8](https://githubja.com/hhatto/autopep8)
- [ESLint](https://eslint.org/)
- [stylelint](https://github.com/stylelint/stylelint)

を使用していて、問題がない場合にのみコミットに含めることができます

逆に、問題がある場合はリポジトリを健全に保つため、問題を修正する必要があります(個別の対応になるので、それぞれ別の場所に書きます)

一時的にチェックを無効化したい場合は、

``` bash
$ git commit -n
```

で諸々を無効化して、コミットすることができます

**本当にやむを得ないときだけ** 使うようにしてください

## テストと Github Actions

テストツールとして、 [pytest](https://docs.pytest.org/en/stable/) を使います(フロント用はまだ準備してないです)

時間がかかって開発者体験が悪くなるので、`Git フックス` で回したりはしませんが、クラウドで [Github Actions](https://github.co.jp/features/actions) を用いて回します

テストが失敗したときは、メールで通知が来ますので、ログ等みながら問題を修正するようにお願いします

テストの書き方等については個別の場所に書きます

## 実行ファイル

既にいくつか出てきてますが、いくつかの実行ファイルを `bin/*.sh` に用意しています

| ファイル名 | 用途 |
| :---: | :--- |
| setup.sh | クローン後の環境構築用 |
| start_db.sh | データベースサーバーの起動 |
| check.sh | 静的解析の実行 |
| sync.sh | パッケージ更新、マイグレーションの適用など(DBコンテナを再起動したときや、ブランチ移動によって依存関係が壊れたときなど) |
| test.sh | ローカルでテストを実行 |

必要に応じて使ってください

## バックエンド開発に関して

バックエンド(Django)の開発に関するルールやガイド等以下にまとめます

### コーディング規約

レビュー等もあまり挟めないと思うので、規約としては `autopep8` の整形と `flake8` のルールのみとします

`import` 文に関してだけ、

``` python
from django.shortcuts import render

from .model import SomeModel
```

のように

``` python
# ライブラリのインポート
# 1行開ける
# 自アプリケーションからのインポート
```

という形式でお願いします

関数やクラスコメントを書く場合は、`Google Style` で統一します([例](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)、参考: [GoogleスタイルのPython Docstringの入門](https://qiita.com/11ohina017/items/118b3b42b612e527dc1d))

推奨にいれてませんが、`VSCode` の [Python Docstring Generator](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring) を使うと形式を自動生成してくれるのでオススメです

### mypy

mypy は型チェックツールです

変数、関数の引数、戻り値等に対して型チェックが行われます。

``` bash
$ ./bin/check。sh
```

でCUIから実行できますが、`VSCode` 拡張が入っていれば教えてくれるのであえて実行する必要はありません

#### 記法

変数に関しては型推論と言って、`x = 10` なら x は `int` 型だろうと補完してくれるので、いつも通り書けば大丈夫です

例外として、ジェネリクス(:=型に情報を付加するもの、例: 配列 ▶ `int` 値を格納する配列)が必要な型をジェネリクスなしで代入するような場合に関しては型付けが必要になります

``` python
from typing import List

age_list: List[int] = []  # List[?] なので型付けが必要
name_list = ['taro']      # List[str] が自明なので不要
```

関数やメソッドに関しては推論ができないので、引数と戻り値の型を書いてください

``` python
def double(x: int) -> int:
    return x ** 2
```

定義したクラスは当然そのまま型として使えます

``` python
class MyInt:
    pass


def double_my_int(x: MyInt) -> MyInt:
    pass
```

ただし、名前解決の順番で問題になることもあります、例えばコピーメソッド。

``` python
class User:
    def __init__(self, name: str) -> None:
        self.name = name

    def copy(self) -> User:  # User が未定義状態なので型チェックはOKだけど、実行時にエラーになる
        return User(name=self.name)
```

こういうときは型名を文字列で書きます

``` python
class User:
    def __init__(self, name: str) -> None:
        self.name = name

    def copy(self) -> 'User':
        return User(name=self.name)
```

他にも、型はかけるが、実行時にPythonがエラーを吐くみたいなケースでは、文字列で囲んで対処することが間々あります

例えば、モデルから取り出したデータリストは `QuerySet` 型で返ってくるんですが、配列同様に型的にはジェネリクスが必要ですが、Pythonランタイムと競合を起こしてしまいます

``` python
from django.db.models.query import QuerySet

from .models import User


def sample(users: QuerySet[User]) -> None:
    """
    [] は本来 イテラブルオブジェクトに対する添字アクセスなので
    QuerySet(Python的にはクラス)に添え字アクセスできないとエラーになる
    """
    pass


def sample2(users: QuerySet) -> None:
    """
    実行は問題なくできるが、
    mypy がジェネリクスを付与しなさいとエラーを起こす
    """
    pass


def sample3(users: 'QuerySet[Model]') -> None:
    # 解決策、シングルクォーテーションで囲む
    pass
```

その他、型付けの拡張は、標準ライブラリの `typing` によって行われます

組み込み以外で型を書くものはたいてい `typing` のものなので、

[typing --- 型ヒントのサポート — Python 3.8.6 ドキュメント](https://docs.python.org/ja/3.8/library/typing.html)

を参考にしてください

各コレクション(`List`, `Dict`, `Tuple`), `Union`, `Optional`, `Any` 辺りは基本的で良く使うので、軽く確認しておいたほうが良いかもです

#### 型エラーを無視する

開発効率が落ちたら元も子もないので、難しそうなときは気軽に `Any` を付与するか、無視することで対応してください！

``` python
from hoge import huga, Foo

from typing import Any


x: Any = huga()  # Any は`制約のない型` を指すので型問題は起きません


class Sample(Foo):  # type: ignore
    """
    type: ignoreを
    """
    pass
```

あまり望ましい状態ではないので、無視するときは事後報告で良いので一言ください！

確認して型を書いておきます

また、 `admin` や `test` にはそもそも型を書く必要はありません

#### ライブラリの型付け

ライブラリには、型付けファイルが提供されていることがあります

例えば、[django-stubs](https://github.com/typeddjango/django-stubs) です

そういう場合は、開発用パッケージに追加してあげるだけでOKです

``` bash
$ pipenv install --dev django-stubs
```

提供されていない場合は、

``` bash
$ pipenv run stubgen <パッケージ名>
# 例
$ pipenv run stubgen allauth
```

で `out` 下にスタブファイルが自動生成されます

厳格なものではないので、

``` ini
[mypy-<パッケージ名>.*]
ignore_errors = True
```

を `mypy.ini` に追加してエラーを無視しておく必要があります

### pytest

このプロジェクトでは、`tests/*.py` の `T_*` クラスの `case_*` 関数をテストとして認識します

テストは各々が必要だと感じたタイミングで書きましょう、カバレッジは求めません

また、テストには一種のドキュメントとしての役割を期待しますので、クラス名及び関数名は日本語を使用するようにしてください

#### ユーザーモデルに対する認証のテスト例

``` python
# accounts/tests/test_models.py
import pytest

from ..models import User


@pytest.fixture  # テストの前後に実行できる関数
def basic_user():
    """
    今回のように、テスト用データを準備する用途でよく使います
    テストデータの作成部分を fixture に共通化しておいて、各テスト関数から呼出すイメージです
    実際の呼び出しは、下のテスト関数を参考にしてください
    """
    return User.objects.create_user(
        email='user@example.com',
        password='password'
    )


@pytest.mark.django_db
class T_ユーザー認証:
    pytestmark = pytest.mark.django_db

    def case_基本(self, basic_user):  # 引数に fixture を渡している
        assert basic_user.check_password('password') == True

    def case_間違ったパスワードの入力(self, basic_user):
        assert basic_user.check_password('missed_password') == False
```

こんな感じで、

- クラス: テストしたい事象
- メソッド: 個別ケース(入力データを変えたり)

という書き方をしていきます

その他、`Django` 特有のテストの書き方がいくつもあります

[pytest-django](https://pytest-django.readthedocs.io/en/latest/) を参考にしてください

※ 時間があれば、`view` のテストサンプルくらいは追加するかもです

#### テストの実行

テストは基本リモートで回しますが、テストを書くときにはローカルで逐次実行したほうが良いと思います

``` bash
$ py.test
```

で実行します

### VSCode によるデバッグ

開発サーバーは、VSCodeのデバッグ構成からも建てることができます

VSCodeの機能を利用すれば、ブレークポイントを使って効率的にデバッグが行えます

参考: [Visual Studio Codeでデバッグをするための基礎知識](https://www.atmarkit.co.jp/ait/articles/1707/21/news030.html)

## フロントエンド開発に関して

フロントエンドでは、[TypeScript](https://www.typescriptlang.org/) と [Sass(Dart)](https://sass-lang.com/dart-sass) を使います

一部、リッチなUIが必要な場合は [svelte](https://svelte.dev/) を使ってますが、基本バニラで書きます

フロント周りの環境は前に書いた [Djangoとwebpackを連携して､ モダンなフロントエンド環境を構築する -- Zenn](https://zenn.dev/kimuson/articles/b2a96d7c8729659379d3) がベースになってるので、詳しく知りたいときはこちらへ。

### 全体用のスクリプトとスタイルを書く

テンプレートの継承元になる `base.html` からは、

- `frontend/static/entries/base.ts`
- `frontend/static/styles/index.scss`

が読まれますので、これらに書いていきます

### 個別のテンプレート用のスクリプトとスタイル

`frontend/static/entries` 下のファイルを元にスタイルシートやスクリプトを読み込むことができます

例えば、`templates/index.html` に

- `static/scripts/entries/index.ts`
- `static/styles/index_page.scss`

を読ませる場合には、以下のようにファイルを準備します

``` html
<!-- index.html -->
{% extends 'base.html' %}
{% load render_bundle from webpack_loader %}

{% block external_header %}
{% render_bundle 'index' 'css' %}
{% endblock %}

{% block content %}
<!-- ... -->
{% endblock %}

{% block external_footer %}
{% render_bundle 'index' 'js' %}
{% endblock %}
```

``` typescript
// entries/index.ts
import "@styles/index_page.scss"

// ...
```

### TypeScript

`TypeScript` は、型付きの `JavaScript` です

mypy 同様に、型付けが難しそうなら `Any` を使ってください(全ての変数に `Any` を付与すれば、JavaScriptと変わりません)

``` typescript
function sample(arg: Any): Any {
  // content
}
```

### SCSS

`SCSS` は、`CSS` の拡張構文で構成されます

色々拡張構文がありますが、あえて導入しているのは、

- 逐次エラー解析が挟まれるので、エラーチェックが捗る
- 変数や計算式を使えるのでDRYにかけてメンテしやすい

辺りが大きいので、特に気にせずCSSをそのまま書けば大丈夫です

変数や計算式は、

``` scss
$-hoge-height: 100px;
$-huga-height: 200px;
$-hoge-huga-height: $-hoge-height + $-huga-height;
```

こんな感じで使えるので、必要に応じて使うと良いと思います

全体で共有する変数(テーマ色とか)は、`styles/_variable.scss` に書いてあります

``` scss
@use "@styles/variable" as var;

.sample {
  background: var.$theme-color;
}
```

こんな感じで使ってください

その他、SCSSの構文は好きに使ってもらってOKですが、ランタイムが `Dart Sass` でもっとも一般的な `node-sass` とは違うので、調べるときにはこの辺に注意してください

### SMACSS

ページ単位でスタイルを書いても大丈夫ですが、共通のコンポーネントには共通のクラスを当てていく(Bootstrapみたいなイメージ)、SMACSSをベースとしたスタイルも用意しています

参考: [SMACSSによるCSSの設計 - ベースとレイアウト | CodeGrid](https://app.codegrid.net/entry/smacss-1)

書き方は任せますが、再利用するクラスを定義するときは SMACSS に従って書いてください
