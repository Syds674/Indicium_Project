# DESAFIO ENGENHARIA DE DADOS INDICIUM 



## Overview
Para a validação do desafio será necessário a construção do ambiente através dos comandos abaixo



##### Clone o repositório em sua máquina local Linux e acesse a pasta Indicium_Project
```sh
git clone https://github.com/Syds674/Indicium_Project.git
```
```sh
cd Indicium_Project
```

##### Para a construção do ambiente, executar:
```sh
sudo docker-compose -f all-docker-compose.yaml up
```

##### Em seguida, para realizar a cópia da estrutura de scripts para dentro do namenode, abra um novo terminal no diretório Indicium_Project e executar: 
```sh
./copy_indicium_structure.sh
```
Obs.: Após a ultima execução irá conectar automáticamente no namenode.


##### Estando conectado no namenode, executar:
```sh
chmod 775 /indicium/cria_dir.sh
```
```sh
./indicium/cria_dir.sh
```
Obs.: Este comando irá criar a estrutura de pastas do HDFS

##### Executar o comando de criação de database no Hive:
```sh
spark-submit /indicium/create_database.py
```


## Etapa do Desafio

### Para a extração dos dados temos a pasta /indicium/scripts contendo os scripts que executarão todo processo de ETL
```
extracao_dados_{nome_tabela}.py
```
- Script que extrai as tabelas da fonte postgres e CSV disponibilizando os arquivos dentro do diretório do hdfs no formato /hdfs/data/order/{nome_tabela}/input/{fonte}_{nome_tabela}_{data}.csv e no diretório local no formato /indicium/data/order/{nome_tabela}/{fonte}_{nome_tabela}_{data}


```
process_{nome_tabela}.py 
```
- Script que lê o arquivo  /hdfs/data/order/{nome_tabela}/input/{fonte}_{nome_tabela}_{data}.csv, grava um backup no diretório do hdfs /hdfs/data/order/{nome_tabela}/backup/ e salva a tabela no hive.


```
create_view_order_details.py 
```
- Script que cria a via de pedidos e seus detalhes


##### Exemplo de execução do scripts
```sh
spark-submit /indicium/scripts/extracao_dados_{nome_tabela}.py YYYY-MM-DD
```
```sh
spark-submit /indicium/scripts/process_{nome_tabela}.py YYYY-MM-DD
```
Obs.: Necessário passar a data como parâmetro no formato YYYY-MM-DD para os scripts extracao_dados_{nome_tabela}.py e process_{nome_tabela}.py

```sh
spark-submit /indicium/scripts/create_view_order_details.py
```



## Para consulta ao Hive e acesso as tabelas, utilize a seguinte URL

|Applicação | Url |
|--- |--- |
| Hue | http://localhost:8888 |

User login: hue
Password: hue

- Para consultar a view view_order_details no hive, execute:
```sh
SELECT * FROM northwind.view_order_details 
```


## Dependências
- [Docker](https://docs.docker.com/):
    1. Install Docker on ubuntu: https://docs.docker.com/engine/install/ubuntu/
    2. Install Docker on windows: https://docs.docker.com/desktop/install/windows-install/
 
## Para a realização deste desafio foi utilizado o repositório:
https://github.com/mrugankray/Big-Data-Cluster
