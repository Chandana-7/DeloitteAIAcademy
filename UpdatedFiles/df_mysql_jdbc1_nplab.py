# This pyspark application connects to a mysql database and loads a table into a dataframe and shows the top 20 rows
# It can be launched or run with the following command

# spark-submit --master yarn --jars /opt/cloudera/parcels/CDH-6.2.1-1.cdh6.2.1.p0.1425774/lib/sqoop/lib/mysql-connector-java-5.1.7/mysql-connector-java-5.1.7-bin.jar df_mysql_jdbc1_nplab.py

import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("PySpark MySQL JDBC example").getOrCreate()

# Following is the syntax to give each option separately.
# Note that driver has to be provided as one of the options because
# pyspark shell is started without the argument --driver-class-path.

df_mysql = spark.read.format("jdbc").option("driver", "com.mysql.jdbc.Driver").option("url", "jdbc:mysql://ip-10-1-1-204.ap-south-1.compute.internal/jigsawdb").option("dbtable", "cctab").option("user", "jigsawuser").option("password","jigsaw321$").load()

# Below is the alternate syntax for the same.
# Instead of .option the parameters are given as a dictionary as key-value pairs

# df_mysql = spark.read.jdbc("jdbc:mysql://ip-10-1-1-204.ap-south-1.compute.internal/", "jigsawdb.cctab", properties={"driver": "com.mysql.jdbc.Driver", "user": "jigsawuser", "password": "jigsaw321$"})

df_mysql.show()
print df_mysql.count(),'**********'
