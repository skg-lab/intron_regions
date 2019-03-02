#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: yyasumizu
# @Date: 2019-02-18
# @Last Modified time: 2019-02-18

'''
usage :
python count_intron.py intron.bed bam output-prefix

ex.
python count_intron.py ref/mm10_genes_intron.bed bam/84_DP_RamDA_test.accept.sort.bam intron_count/84_DP_RamDA_test

ipynb for the data prep : /home/yyasumizu/RAID6TB/bioinformatics/mac/SingleCell/ramda/intron_count.ipynb
'''


import os
import sys
import pandas as pd
import pybedtools as pb


f_bed_intron = sys.argv[1]
f_bam = sys.argv[2]
f_out_prefix = sys.argv[3]


ref = pb.BedTool(f_bed_intron)
bam = pb.BedTool(f_bam)
counts = ref.coverage(bam, s=True) # only the same strand

bam_count = bam.count()

df_count = counts.to_dataframe()
df_count.columns = ['chr', 'start', 'end', 'symbol', 'score', 'strand', 'n_overlap', 'len_overlap', 'len', 'frac']

df_count_groupby = df_count.groupby('symbol').sum()
df_count_groupby['symbol'] = df_count_groupby.index

df_count_groupby['rpkm'] = df_count_groupby['n_overlap'] / (df_count_groupby['len'] / 1000) * (bam_count / 1000000)


df_count_groupby[['symbol', 'rpkm']].to_csv(f_out_prefix+'RPKM.txt', index=None, header=None, sep='\t')
df_count_groupby[['symbol', 'n_overlap']].to_csv(f_out_prefix+'count.txt', index=None, header=None, sep='\t')
