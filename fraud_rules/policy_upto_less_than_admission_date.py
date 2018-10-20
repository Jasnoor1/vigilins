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
policy_upto_less_than_admission_date = session.sql(""" select `Policy Upto`,`Admission date` from global_temp.my_table where `Policy Upto` < `Admission date` """)
policy_upto_less_than_admission_date.show()

