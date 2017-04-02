#!/bin/bash

hdfs dfs -rm -r /user/$USER/ex2/${USER}_task_3.1.out

hadoop jar /opt/hadoop/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
-D mapreduce.job.name.job.name='kuddai job' \
-D mapreduce.job.reduces=10 \
-input  /data/assignments/ex2/task2/logsLarge.txt   \
-output /user/$USER/ex2/${USER}_task_3.1.out \
-mapper mapper.py \
-combiner reducer.py \
-reducer reducer.py \
-file mapper.py \
-file reducer.py \
-file combiner.py

echo 'the result in the /user/$USER/ex2/${USER}_task_3.1.out is num_reduces so I can do it via awk'

hdfs dfs -cat /user/$USER/ex2/${USER}_task_3.1.out/* | awk '$2 > x{x=$2; y=$0};END{print y}' > result.txt


