
# Codoner
Codoner = Codon + Encoder = Codon + Protector

システム上で使用する暗号化システムに、mRNAコドンの仕組みを応用する研究です

## Site Links
webサイト適当に作りました！

[codoner -home- ](https://citrus-mizuha.github.io/codoner.github.io/)

Discordサーバーのリンクも貼っておくので、ぜひ、興味がある方は参加してください！<br>お待ちしております

[Discord - Codoner](https://discord.com/invite/EYJjRNzRQE)

## 前提知識 (高校生物基礎の内容)
### セントラルドグマ

1. DNAが存在
2. そのDNAの片方をもとにmRNAに転写
3. そのmRNAをもとにtRNAがアミノ酸を配列させる

この一連の流れのことをセントラルドグマと呼ぶ

なお、DNAは二重螺旋構造 (2本)、RNAは一本鎖構造をしていることが多い

### DNAとは
DeoxyriboNucleic Acid

デオキシリボースを糖として持ち、塩基に"A", "T", "G", "C" を持つものである
- A : アデニン
- T : チミン
- G : グアニン
- C : シトシン

AとTが水素二重結合、GとCが水素3重結合で連結しており、塩基の相補性を担保している

構造体としては、デオキシリボースと、塩基とリン酸を合わせたものを**ヌクレオチド**と呼ぶ

これが鎖状になっているものを、**ヌクレオチド鎖**と呼ぶ

そのうち、生命活動などに必要な部分の情報を**遺伝子**と呼ぶことがあり、遺伝子はDNA全体の1.5%ほどである (**エキソン**と呼ばれる)

そのほかの98.5%には、**イントロン**と呼ばれる部分と、その他の塩基配列がある

### RNAとは
RiboNucleic acid

DNAとは違って、糖はリボースである

また、塩基は、A, **U**, G, C で構成される

- A : アデニン
- U : ウラシル
- G : グアニン
- C : シトシン

AとUが水素二重結合、GとCが水素3重結合で連結しており、塩基の相補性を担保している

RNAにおいてもヌクレオチドとヌクレオチド鎖の名称は使用される

RNAは、DNAを元に転写されたものを使ってタンパク質のアミノ酸配列を決定したりするものである

よく出てくるRNAとして**mRNA**と**tRNA**がある

### DNA->mRNA->タンパク質
DNAの塩基配列は、以下のような仕組みになっている
例） (XとYが向き合って一本の2重螺旋構造のDNAを成しているものとする)
```python
--------------------------------------------- X
ATGCGCATACGTCAGAAAGCTGACGTAGCCCGTGTGTGATTTACT
|||||||||||||||||||||||||||||||||||||||||||||
TACGCGTATGCAGTCTTTCGACTGCATCGGGCACACACTAAATGA
--------------------------------------------- Y
```
次に、このDNAの水素結合( `|` で表しているもの)

この時、Yの方を鋳型としてmRNAを作成することになったとする
すると、以下のようになる
```python
DNA鎖 "Y" : TAC, GCG, TAT, GCA, GTC, TTT, CGA, CTG, CAT, CGG, GCA, CAC, ACT, AAA, TGA

↓ 転写

mRNA鎖    : AUG, CGC, AUA, CGU, CAG, AAA, GCU, GAC, GUA, GCC, CGU, GUG, UGA, UUU, ACU
# 今回はないが、実際の転写の際は、転写の過程で大量のイントロンがスプライシングされ、エキソンのみの情報に書き換えられる

↓ 翻訳 # コドンという、3文字の延期で一つのアミノ酸を指定している仕組みを利用して、アミノ酸配列に変換 (翻訳) できる

アミノ酸配列: Met - Arg - Ile - Arg - Gln - Lys - Ala - Asp - Val - Ala - Arg - Val - Stop
```
このmRNA鎖からアミノ酸配列に翻訳される時には、**tRNA**という別のRNA組織が関わっている

また、鎖XとYのどちらを鋳型として使用するかは、**鋳型鎖**がどちらであるかが関わっている。

遺伝子発現の時は、**アンチセンス鎖**側が鋳型となる

### コドン表
mRNAのコドンが何のアミノ酸を指定するか分かりやすくまとめた表である
今回の研究において重要なのは、このコドンの仕組みである
**アミノ酸の数は、20個であるが、コドンは最大**$4^3 = 64$**通りを表現することが可能である**
この特性と、イントロンの存在は、外的要因(ウイルスなど)に対する順応とも言われるように、外的破壊や改ざんに対する対策として有効である

## 研究概要
当研究は、DNAの仕組みを応用すれば、[コドン表](#コドン表) の項目にて明記した通り、外的破壊や改ざんに対する耐性を暗号化方法自体に持たせることが可能なのではないか、という仮説のもと行う
### 仕組み(イメージ)
以下のような2進数に変換したデータがあったとする
(可読性を上げるために"_"を用いている)
```python
2進数 : 0000_1100_1010_0110_1010_0101_1111_0110_1010_1110
↓ 変換
10進数:  0    12   10    6   10   5    15   6    10   14
```
この10進数データ (16通り) と、`S`１パターンと`F`4パターンの計21パターンに対して、コドンを割り当てる

ただし、固定要素として、本来のDNA構造とは異なるが、`Start`と`Finish` (以下 `S`, `F`) に関しては、Sは1つ、Fは4パターンを固定で割り当てる。
```math
S = [x]
```
```math
F = [a, b, c, d]
```
この時、`x`と`a, b, c, d`などの記号部分は端末z固有の「コドン表」を作成し、それに基づいて行われるものとする

```math
(64-4-1)÷16 = 3...11
```
***
通し番号0 ~ 17を使用し、
0~15までは、それぞれに3個ずつコドンを割り振り、追加で11個分を割り振る

また、16番は、Startとし、この枠のコドンは一つのみとする

最後に、17番には、必ず4つのコドンを割り振ることとする
***
このように、**割り振る**

このコドン表自体をクラインアント側で乱数で生成し、複合鍵は現状未決定ではあるが、独自の型を作ろうと思う

また、このATGCの状態が分かりやすいため、ここまでAUGCで述べてきたが、実際に保存するときは順に、(0,1,2,3)で保存し、これを2進数に変換して使用するものとする

## 結果的な流れ
1. データを2進数に変換
2. 2進数データを4bit区切りにして10進数に変換
3. セッションごとに「コドン表」(`codon_0`)を作成、使用して疑似4進数に変換
4. 「コドン表」を新たに生成(`codon_1`, `codon_2`...)して、Codon to Codonの処理を繰り返す

   (n回処理を行った時、4bit平文に対して$4^n$通りの表現方法が存在するため、例えば、64回以上行えば、$`4^{64} = 2^{128}`$となり、ブルートフォース対策としても十分なはずである)
5. 生成された擬似4進数を数として扱って2進数に変換 or `codon_m`(m番目のcodon表 mは乱数で求める)を利用して逆算的に2進数に変換
6. 完成！(6bitを平文4bitとして出力することになる)

## Version Models
|Ver|日付|時間|詳細(変更点)|CommitHash|
|---|---|---|---|---|
|0.0.0|2024/7/11|14:00|初版|???|
