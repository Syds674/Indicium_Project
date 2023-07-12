from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import argparse

parser = argparse.ArgumentParser()       
parser.add_argument("data_processamento", help="FORMATO ACEITAVEL: YYYY-MM-DD",  )
args = parser.parse_args()


spark = SparkSession \
    .builder \
    .master("yarn") \
    .appName("Ingestao - dados") \
    .enableHiveSupport() \
    .getOrCreate()

def get_file_hdfs(file_name, fonte, data_processamento):
    
    df = spark.read.csv("/hdfs/data/order/{}/input/{}_{}_{}.csv/*.csv".format(file_name, fonte, file_name, data_processamento), header=True)
    
    return df

def backup_file_hdfs(file_name, fonte, df, data_processamento):
  
    df.coalesce(1).write.mode('overwrite').option('header','true').csv('/hdfs/data/order/{}/backup/{}_{}_{}.csv'.format(file_name, fonte, file_name, data_processamento))


def save_as_table(file_name, fonte, df):

    df.write.mode('overwrite').format('orc').saveAsTable("northwind.{}".format(file_name), path="/hdfs/data/order/processed/{}".format(file_name))
    
    print("northwind.{} Atualizada".format(file_name))

fonte = 'postgres'
file_name = 'employees'



try:
    
    print("OBTENDO ARQUIVO HDFS PARA DATA: {}".format(args.data_processamento))
    df = get_file_hdfs(file_name, fonte, args.data_processamento)
    
    #Realiza o backup do arquivo no folder backup no hdfs pois a ideia e que exista o script que faz a limpeza dos arquivos do diretorio input  
    print("GERANDO BACKUP DO ARQUIVO: {}.csv".format(file_name))
    backup_file_hdfs(file_name, fonte, df, args.data_processamento)
    
    print("GRAVANDO TABELA {}".format(file_name))
    save_as_table(file_name, fonte, df)
        
except Exception as e:
    print("ERRO:", e)
