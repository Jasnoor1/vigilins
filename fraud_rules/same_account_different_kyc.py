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
same_account_different_bank_name = session.sql("""select `Account No` ,COUNT(*) from global_temp.my_table GROUP BY `Account No`  HAVING COUNT(DISTINCT `Bank Name`)>1""")
same_account_different_bank_name.show()


