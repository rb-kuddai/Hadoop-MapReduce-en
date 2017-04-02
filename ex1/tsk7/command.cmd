hadoop jar /opt/hadoop/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator -D stream.num.map.output.key.fields=2 -D mapreduce.partition.keypartitioner.options=-k1,2 -D mapreduce.partition.keycomparator.options="-k1,1n -k2,2n"  -input /data/assignments/ex1/matrixLarge.txt  -output /user/$USER/data/output/ex1/s1569105_task_7.out -mapper mapper.py -reducer reducer.py -file mapper.py -file reducer.py -jobconf mapred.reduce.tasks=1 -jobconf mapred.job.name="kuddai job"
