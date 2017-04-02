hdfs dfs -rm -r /user/$USER/ex2/${USER}_task_4.3.0_small.out

hadoop jar /opt/hadoop/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
-D mapreduce.job.name.job.name='kuddai job' \
-D mapreduce.job.reduces=1 \
-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
-D mapreduce.partition.keypartitioner.options=-k1,1 \
-D mapreduce.partition.keycomparator.options="-k1,1 -k2,2" \
-D stream.num.map.output.key.fields=2 \
-D num.key.fields.for.partition=1 \
-input  /data/assignments/ex2/task3/stackSmall.txt  \
-output /user/$USER/ex2/${USER}_task_4.3.0_small.out \
-mapper mapper0.py \
-reducer reducer0.py \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
-file mapper0.py \
-file reducer0.py

rm ./${USER}_task_4.3.0_small.out

hdfs dfs -getmerge /user/$USER/ex2/${USER}_task_4.3.0_small.out ./${USER}_task_4.3.0_small.out