#!/bin/bash
for filename in test_res/*.txt; do
    ##### convert the output to TREC format #####
    name="${filename%.*}"
    TREC_DATA="$name.trec_eval"
    perl convertWekaOutputToTRECFormat.pl $filename test_res/test-less-than-40.xml > $TREC_DATA 2>/dev/null

    ##### evaluate #####
    echo "TREC Scores of $name:"
    TREC_OUT="$name.trec_out"
    trec_eval-8.0/trec_eval -q -c ./eval/Test-T40.judgment $TREC_DATA > $TREC_OUT
    grep -E -w 'map.*all|recip_rank.*all' $TREC_OUT

done