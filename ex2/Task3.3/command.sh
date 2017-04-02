#!/bin/bash

hdfs dfs -rm -r /user/$USER/ex2/${USER}_task_3.3.out

hadoop jar /opt/hadoop/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
-D mapreduce.job.name.job.name='kuddai job' \
-D mapreduce.job.reduces=10 \
-input  /data/assignments/ex2/task2/logsLarge.txt   \
-output /user/$USER/ex2/${USER}_task_3.3.out \
-mapper mapper.py \
-combiner combiner.py \
-reducer reducer.py \
-file mapper.py \
-file combiner.py \
-file reducer.py

hdfs dfs -cat /user/$USER/ex2/${USER}_task_3.3.out/part-00000 | head -10 > result.txt

rm ./${USER}_task_3.3.out
hdfs dfs -getmerge  /user/$USER/ex2/${USER}_task_3.3.out ./${USER}_task_3.3.out