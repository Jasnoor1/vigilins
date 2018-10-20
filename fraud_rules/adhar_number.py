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
adhar = session.sql(""" select `Aadhar Number` from global_temp.my_table where `Aadhar Number` IS NOT NULL and LENGTH(`Aadhar Number`) != 12  and `Aadhar Number` RLIKE '[a-zA-Z].*'""")
#adhar_filter = adhar.filter("`Aadhar Number`= [a-z]").show()
adhar.show()

