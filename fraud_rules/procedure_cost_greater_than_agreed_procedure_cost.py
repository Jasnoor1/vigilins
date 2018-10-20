
from pyspark.sql import SparkSession
import pandas as pd
#from pyspark import SQLContext
from pyspark import SparkContext
from pyspark.sql import Row
import csv
from pyspark import SQLContext
from pyspark.sql.functions import regexp_extract
import re

session = SparkSession.builder.appName("claims").master("local[1]").getOrCreate()
dataFrameReader = session.read
responses = dataFrameReader.option("header","true").option("inferSchema",value=True).csv("/home/naboo/csvfile.csv")
responses.createGlobalTempView('my_table')
#d = session.sql(""" select * from global_temp.my_table """)
claim_amount_greater_than_amount_recomended = session.sql(""" select `Claim Amount`,`Amount Recommended` from global_temp.my_table where `Claim Amount` > `Amount Recommended`  """)
claim_amount_greater_than_amount_recomended.show()

