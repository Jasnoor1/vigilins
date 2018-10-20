from pyspark.sql import SparkSession
import pandas as pd
#from pyspark import SQLContext
from pyspark import SparkContext
from pyspark.sql import Row
import csv
from pyspark import SQLContext


session = SparkSession.builder.appName("claims").master("local[1]").getOrCreate()
dataFrameReader = session.read
responses = dataFrameReader.option("header","true").option("inferSchema",value=True).csv("/home/naboo/csvfile.csv")
responses.createGlobalTempView('my_table')
a=session.sql("select * from global_temp.my_table")
a.show()
claim_more_than_one_time_in_a_year=session.sql("""select `Account No`,`year`,COUNT(*) from global_temp.my_table GROUP BY `Account No`,`year` HAVING COUNT(`Account No`)>1 """)
claim_more_than_one_time_in_a_year.show()
#a.write.format("csv").option("useHeader","true").save("/home/naboo/e.csv")

