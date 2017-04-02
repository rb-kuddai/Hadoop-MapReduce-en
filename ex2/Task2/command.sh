#!/bin/bash

hdfs dfs -rm -r /user/$USER/ex2/${USER}_task_1.out

hadoop jar /opt/hadoop/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
-D mapreduce.job.name.job.name='kuddai job' \
-D mapreduce.job.reduces=1 \
-input  /user/$USER/ex2/${USER}_task_1.out  \
-output /user/$USER/ex2/${USER}_task_2.out \
-mapper mapper.py \
-reducer reducer.py \
-file reducer.py \
-file mapper.py \
-file terms.txt

hdfs dfs -cat /user/$USER/ex2/${USER}_task_2.out/part-00000 | head -10 > result.txt

rm ./${USER}_task_2.out
hdfs dfs -getmerge  /user/$USER/ex2/${USER}_task_2.out ./${USER}_task_2.out