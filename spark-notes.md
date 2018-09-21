# Spark Notes

## Installating Spark
- Follow this guide to install Spark: https://datawookie.netlify.com/blog/2017/07/installing-spark-on-ubuntu/
- Install pyspark in conda environment: `pip install pyspark`

## Spark in Jupyter Notebook
- Use `findspark`
- `pip install findspark`
- `import findspark`
- `findspark.init("/usr/local/spark")` # If followed directions above
- Additional info at https://datawookie.netlify.com/blog/2017/07/accessing-pyspark-from-a-jupyter-notebook/

- Spark should now be running

## Connect local machine to ports for monitoring
ssh -i "private_key.pem" server -L localport:localhost:serverport
- 8080 is master port and 4040 shows jobs

## Starting Spark cluster
- First need to allow local ssh
- `ssh-keygen -t rsa -P ""`
- `cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys`
- Then start the master and workers
    - `/usr/local/spark/sbin/start-all.sh`
    - Navigate to localhost:8080
    - Find the URL for the cluster: `spark://ip-172-31-23-133.ec2.internal:7077`

## Connecting to Spark Cluster in Python
- `import pyspark`
- `sc = pyspark.SparkContext(master = 'cluster url')`

## Using Logging
- localhost:4040 is only available while job is running
- save log file by setting conf

```python
conf = pyspark.SparkConf()
conf.set('spark.eventLog.enabled', True)
conf.set('spark.eventLog.dir', '/usr/local/spark/tmp')
```
- Specify conf file when setting a SparkContext
```python
sc = pyspark.SparkContext(master = 'cluster_url',
                          conf = conf,
                          appName = 'testing')
```

- Read in `json` log into dataframe using
`pd.read_json('log_file', lines = True)`

## S3 uploads

* Configure account using `aws configure`
* Access key id and secret are in `credentials.csv`
* Upload with `aws s3 cp folder s3://bucket/ --recursive`
* `--recursive` is necessary for folders

