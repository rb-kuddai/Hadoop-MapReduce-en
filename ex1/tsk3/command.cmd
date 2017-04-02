cat s1569105_task_3.out | ./combine.py > s1569105_task_3_final.out
hadoop jar /opt/hadoop/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -input /user/$USER/data/output/ex1/s1569105_task_2.out -output /user/$USER/data/output/ex1/s1569105_task_3.out -mapper /bin/cat -reducer reducer.py -file reducer.py -jobconf mapred.reduce.tasks=2 -jobconf mapred.job.name="kuddai job"
