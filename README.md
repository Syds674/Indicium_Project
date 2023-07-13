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

##### Para realizar a cópia da estrutura de scripts para dentro do namenode, abra um novo terminal no diretório Indicium_Project e executar: 
```sh
./copy_indicium_structure.sh
```
Obs.: Após a ultima execução irá conectar automáticamente no namenode.


##### Estando conectado no namenode, executar:
```sh
./indicium/cria_dir.sh
```
Obs.: Este comando irá criar a estrutura de pastas do HDFS




## Acesse o ecossistema hadoop
Esta é uma lista de tecnologias ou estruturas expostas ao Host. Você pode acessá-los usando os seguintes URLs.
|Applicação | Url |
|--- |--- |
| Namenode UI | http://localhost:9870/dfshealth.html#tab-overview |
| Namenode(IPC port) | http://localhost:9000 |
| History server | http://localhost:8188/applicationhistory |
| Datanode | http://localhost:9864/ |
| Nodemanager | http://localhost:8042/node |
| Resource manager | http://localhost:8088/ |
| Hue | http://localhost:8888 |
| Spark Master UI | http://localhost:8080 |
| Spark Slave UI | http://localhost:8081 |
| Spark Driver UI | http://localhost:4040 (accessible only after a driver is started) |
| Zeppelin UI | http://localhost:8082 |
| Airflow UI | http://localhost:3000 |
| pgAdmin UI | http://localhost:5000 |
| Zookeeper|  http://localhost:2181 |
| kafka broker | http://localhost:9092 |
| Schema Registry | http://localhost:8083 |
| Kadmin UI | http://localhost:8084/kadmin/ |
| Kafka Control Center | http://localhost:9021 |

## Dependências
- [Docker](https://docs.docker.com/):
    1. Install Docker on ubuntu: https://docs.docker.com/engine/install/ubuntu/
    2. Install Docker on windows: https://docs.docker.com/desktop/install/windows-install/
 
## Para a realização deste desafio foi utilizado o repositório:
https://github.com/mrugankray/Big-Data-Cluster
