hdfs dfs -rm -r /user/$USER/ex2/${USER}_task_2_small.out

hadoop jar /opt/hadoop/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
-D mapreduce.job.name.job.name='kuddai job' \
-D mapreduce.job.reduces=1 \
-input  /user/$USER/ex2/${USER}_task_1_small.out  \
-output /user/$USER/ex2/${USER}_task_2_small.out \
-mapper mapper.py \
-reducer reducer.py \
-file mapper.py \
-file reducer.py \
-file terms.txt

rm ./${USER}_task_2_small.out

hdfs dfs -getmerge  /user/$USER/ex2/${USER}_task_2_small.out ./${USER}_task_2_small.out

hdfs dfs -cat /user/$USER/ex2/${USER}_task_2_small.out/part-00000 | head -10 > result_small.txt