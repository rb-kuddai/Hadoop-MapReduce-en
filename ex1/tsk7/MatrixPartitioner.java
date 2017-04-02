import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.JobConf;
import org.apache.hadoop.mapred.Partitioner;
import java.lang.Math;

public class MatrixPartitioner implements Partitioner<Text, Text> {
	//thanks him for example of custom partitioner
	//http://wiki.pentaho.com/display/BAD/Using+a+Custom+Partitioner+in+Pentaho+MapReduce

	//given in the task 6
	public int NUM_COLUMNS;

	public void configure(JobConf job) {
		NUM_COLUMNS = Integer.parseInt(job.get("num_total_columns"));
	}

	public int getPartition(Text key, Text value, int numReduceTasks) {
		int columns_per_reducer = NUM_COLUMNS / numReduceTasks;
		String sKey = key.toString();
		String[] splits=sKey.split("\t"); //Split the key on tab
		int column = Integer.parseInt(splits[0]); //column key
		//min to ensure that we stay within the boundaries
		//although the last reducer will receive slighltly more data points
		return Math.min(column / columns_per_reducer, numReduceTasks - 1);
	}
}
