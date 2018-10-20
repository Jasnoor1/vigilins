from pyspark.sql import SparkSession
import pandas as pd
#from pyspark import SQLContext
from pyspark import SparkContext
from pyspark.sql import Row
import csv
from pyspark import SQLContext
#from pyspark.sql.functions import regex
import re

session = SparkSession.builder.appName("claims").master("local[1]").getOrCreate()
dataFrameReader = session.read
responses = dataFrameReader.option("header","true").option("inferSchema",value=True).csv("/home/naboo/csvfile.csv")
responses.createGlobalTempView('my_table')
pan = session.sql(""" select `Pan no` from global_temp.my_table where `Pan no` IS NOT NULL and LENGTH(`Pan no`) != 10 and `Pan no` NOT RLIKE '[A-Z]{5}[0-9]{4}[A-Z]'  """)
#pan = session.sql(""" select `Pan no` from global_temp.my_table where `Pan no` NOT RLIKE '[A-Z]{5}[0-9]{4}[A-Z]' """)

pan.show()
