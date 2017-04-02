#!/bin/bash

hdfs dfs -rm -r /user/$USER/ex2/${USER}_task_4.3.0.out

echo 'FIRST CYCLE. PRODUCING CLEARED DATASET OF OWNER ID, ACCEPTED ANSWER ID'

hadoop jar /opt/hadoop/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
-D mapreduce.job.name.job.name='kuddai job' \
-D mapreduce.job.reduces=10 \
-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
-D mapreduce.partition.keypartitioner.options=-k1,1 \
-D mapreduce.partition.keycomparator.options="-k1,1 -k2,2" \
-D stream.num.map.output.key.fields=2 \
-D num.key.fields.for.partition=1 \
-input  /data/assignments/ex2/task3/stackLarge.txt  \
-output /user/$USER/ex2/${USER}_task_4.3.0.out \
-mapper mapper0.py \
-reducer reducer0.py \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
-file mapper0.py \
-file reducer0.py

hdfs dfs -rm -r /user/$USER/ex2/${USER}_task_4.3.1.out

echo 'SECOND CYCLE. REDUCER SIDE JOIN. OUTPUTS GUYS WITH MAXIMUM ACCEPTED ANSWERS'

hadoop jar /opt/hadoop/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
-D mapreduce.job.name.job.name='kuddai job' \
-D mapreduce.job.reduces=10 \
-input  /user/$USER/ex2/${USER}_task_4.3.0.out  \
-output /user/$USER/ex2/${USER}_task_4.3.1.out \
-mapper mapper1.py \
-combiner combiner1.py \
-reducer reducer1.py \
-file mapper1.py \
-file reducer1.py \
-file combiner1.py

echo 'the result in the /user/$USER/ex2/${USER}_task_4.3.1.out is num_reduces so I can do it via awk'

hdfs dfs -cat /user/$USER/ex2/${USER}_task_4.3.1.out/* | awk '$2 > x{x=$2; y=$0};END{print y}' > max_user.txt

hdfs dfs -rm -r /user/$USER/ex2/${USER}_task_4.3.out

echo 'THIRD CYCYLE. OUR TASK OUTPUT'

hadoop jar /opt/hadoop/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
-D mapreduce.job.name.job.name='kuddai job' \
-D mapreduce.job.reduces=1 \
-input  /user/$USER/ex2/${USER}_task_4.3.0.out  \
-output /user/$USER/ex2/${USER}_task_4.3.out \
-mapper mapper2.py \
-reducer reducer2.py \
-file reducer2.py \
-file mapper2.py \
-file max_user.txt

hdfs dfs -cat /user/$USER/ex2/${USER}_task_4.3.out/part-00000 | head -10 > result.txt