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
