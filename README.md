# intron_regions

extract intron regions from gtf files and count reads in introns. Use [Gencode](https://www.gencodegenes.org/)!

## Usage

### 1. Intron bedの作成

intron_count.ipynb

### 2. Count reads in the intron bed.

```
python count_intron.py intron.bed bam output-prefix
```

example

```
python count_intron.py ref/mm10_genes_intron.bed bam/84_DP_RamDA_test.accept.sort.bam intron_count/84_DP_RamDA_test
```

## What's new

- 2019/03/01　レポジトリ作成

## for lab members

### githubの使い方

まずは最も基本的なところになれましょう。

- clone : リモートレポジトリをローカルにクローンする。
- fetch or pull : ローカルを最新版に
- add : ステージに変更箇所をあげる。allでも出来るし、変えたいファイル岳も帰れる。
- commit : ステージに上った変更箇所を記録する。
- push : リモートに変更を反映する。

"add -> commit -> push"の流れを押さえてください。


### 具体的な話

- ファイル一つや一日の終りなど、切のいいところでコードをあげる。
- **作業は必ずローカルでやってpush。**
- テストデータなどは`.gitignore`に記録して、リモートにあげないようにする。
- やり方は、github Desktopが最初はおすすめ。atom上でも出来る。vscodeもいいらしいが使ったことがなくわからず。
- [Hydrogen](https://github.com/nteract/hydrogen#how-it-works)というpackageをatomに入れるとjupyterもうごく。ややめんどくさいが。
- ただ、atomはパッケージをどんどん入れるとどんどん重くなるので注意。
- CLI環境では`git`コマンドを使ってください。(see links below.)
- branchの話やfork, pull request(いわゆるプルリク)はおいおい。

#### 参考資料

- [今さら聞けない！GitHubの使い方【超初心者向け】](https://techacademy.jp/magazine/6235)
- [今日からはじめるGitHub 〜 初心者がGitをインストールして、プルリクできるようになるまでを解説](https://employment.en-japan.com/engineerhub/entry/2017/01/31/110000)

他にも、書籍やいろんなサイトがあるので、わからないことがあれば調べてみてください。
