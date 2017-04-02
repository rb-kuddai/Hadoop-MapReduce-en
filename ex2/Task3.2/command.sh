#!/bin/bash

hdfs dfs -rm -r /user/$USER/ex2/${USER}_task_3.2_raw.out

hadoop jar /opt/hadoop/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
-D mapreduce.job.name.job.name='kuddai job' \
-D mapreduce.job.reduces=15 \
-input  /data/assignments/ex2/task2/logsLarge.txt   \
-output /user/$USER/ex2/${USER}_task_3.2_raw.out \
-mapper mapper.py \
-combiner combiner.py \
-reducer reducer.py \
-file mapper.py \
-file combiner.py \
-file reducer.py

hdfs dfs -rm -r /user/$USER/ex2/${USER}_task_3.2.out

hadoop jar /opt/hadoop/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
-D mapreduce.job.name.job.name='kuddai job' \
-D mapreduce.job.reduces=1 \
-input  /user/$USER/ex2/${USER}_task_3.2_raw.out   \
-output /user/$USER/ex2/${USER}_task_3.2.out \
-mapper /bin/cat \
-reducer reducer.py \
-file reducer.py

hdfs dfs -cat /user/$USER/ex2/${USER}_task_3.2.out/part-00000 | head -10 > result.txt

rm ./${USER}_task_3.2.out
hdfs dfs -getmerge  /user/$USER/ex2/${USER}_task_3.2.out ./${USER}_task_3.2.out