#!/bin/bash

hdfs dfs -rm -r /user/$USER/ex2/${USER}_task_1_raw.out

hadoop jar /opt/hadoop/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
-D mapreduce.job.name.job.name='kuddai job' \
-D mapreduce.job.reduces=10 \
-input /data/assignments/ex2/task1/large/  \
-output /user/$USER/ex2/${USER}_task_1_raw.out \
-mapper mapper.py \
-combiner combiner.py \
-reducer reducer.py \
-file mapper.py \
-file combiner.py \
-file reducer.py

hdfs dfs -rm -r /user/$USER/ex2/${USER}_task_1.out

hadoop jar /opt/hadoop/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
-D mapreduce.job.name.job.name='kuddai job' \
-D mapreduce.job.reduces=1 \
-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
-D mapreduce.map.output.key.field.separator=" " \
-D stream.map.output.field.separator=" " \
-D stream.num.map.output.key.fields=1 \
-D num.key.fields.for.partition=1 \
-input  /user/$USER/ex2/${USER}_task_1_raw.out  \
-output /user/$USER/ex2/${USER}_task_1.out \
-mapper /bin/cat \
-reducer /bin/cat \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

hdfs dfs -cat /user/$USER/ex2/${USER}_task_1.out/part-00000 | head -10 > result.txt

rm ./${USER}_task_1.out
hdfs dfs -getmerge  /user/$USER/ex2/${USER}_task_1.out ./${USER}_task_1.out