from pyspark.sql import SparkSession
import argparse
from datetime import datetime, date

parser = argparse.ArgumentParser()       
parser.add_argument("data_processamento", help="FORMATO ACEITAVEL: YYYY-MM-DD",  )
args = parser.parse_args()



def get_postgres(table_name):
    spark = SparkSession.builder \
    .appName("Get - PostgreSQL") \
    .config("spark.jars", "/indicium/postgresql-42.6.0.jar") \
    .getOrCreate()

    url = "jdbc:postgresql://external_postgres_db:5432/northwind"

    properties = {
    "user": "northwind_user",
    "password": "thewindisblowing",
    "driver": "org.postgresql.Driver"}

    df = spark.read.jdbc(url, table_name, properties=properties)
    
    return df


def get_csv(file_name):
    spark = SparkSession.builder.appName('Get - CSV').getOrCreate()
  
    df = spark.read.format("csv").option("header", True).load("file:/indicium/{}.csv".format(file_name))
    
    return df



fonte = 'postgres'
table_name = 'suppliers'
file_name = ''



try:
    if fonte == 'postgres':
        print("EXTRAINDO DO POSTGRES PARA DATA: {}".format(args.data_processamento))
        df = get_postgres(table_name)
        
        #salva o csv no hdfs
        df.coalesce(1).write.mode('overwrite').option('header','true').csv('/hdfs/data/order/{}/input/{}_{}_{}.csv'.format(table_name, fonte, table_name, args.data_processamento))
        #salva o csv no disco local 
        df.coalesce(1).write.mode('overwrite').option('header','true').csv('file:/indicium/data/order/{}/{}_{}_{}'.format(table_name, fonte, table_name, args.data_processamento))
    
    elif fonte == 'csv':
        print("EXTRAINDO DO CSV PARA DATA: {}".format(args.data_processamento))
        df = get_csv(file_name)
                                                                           
        #salva o csv no hdfs                                                                   
        df.coalesce(1).write.mode('overwrite').option('header','true').csv('/hdfs/data/order/{}/input/{}_{}_{}.csv'.format(file_name, fonte, file_name, args.data_processamento))
        #salva o csv no disco local 
        df.coalesce(1).write.mode('overwrite').option('header','true').csv('file:/indicium/data/order/{}/{}_{}_{}'.format(file_name, fonte, file_name, args.data_processamento))
        
except Exception as e:
    print("ERRO:", e)