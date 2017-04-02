#!/bin/bash

hdfs dfs -rm -r /user/$USER/ex2/${USER}_task_4.2.1.out

hadoop jar /opt/hadoop/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
-D mapreduce.job.name.job.name='kuddai job' \
-D mapreduce.job.reduces=10 \
-input  /data/assignments/ex2/task3/stackLarge.txt  \
-output /user/$USER/ex2/${USER}_task_4.2.1.out \
-mapper mapper1.py \
-combiner combiner1.py \
-reducer reducer1.py \
-file mapper1.py \
-file reducer1.py \
-file combiner1.py

echo 'the result in the /user/$USER/ex2/${USER}_task_4.2.1.out is num_reduces so I can do it via awk'

hdfs dfs -cat /user/$USER/ex2/${USER}_task_4.2.1.out/* | awk '$2 > x{x=$2; y=$0};END{print y}' > max_user.txt

hdfs dfs -rm -r /user/$USER/ex2/${USER}_task_4.2.out

hadoop jar /opt/hadoop/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
-D mapreduce.job.name.job.name='kuddai job' \
-D mapreduce.job.reduces=1 \
-input  /data/assignments/ex2/task3/stackLarge.txt  \
-output /user/$USER/ex2/${USER}_task_4.2.out \
-mapper mapper2.py \
-reducer reducer2.py \
-file reducer2.py \
-file mapper2.py \
-file max_user.txt

hdfs dfs -cat /user/$USER/ex2/${USER}_task_4.2.out/part-00000 | head -10 > result.txt