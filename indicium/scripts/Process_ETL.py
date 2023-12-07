import subprocess
from datetime import datetime

# Obtem a data atual no formato YYYY-MM-DD
data_atual = datetime.now().strftime('%Y-%m-%d')

# Caminho do script spark-submit
spark_script = "/indicium/scripts/extracao_dados_order_details.py"

# Lista de scripts a serem executados na ordem desejada
scripts_to_run = [f"spark-submit {spark_script} {data_atual}"]

for script in scripts_to_run:
    try:
        # Execute o script usando subprocess.run
        subprocess.run(script, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        # Se ocorrer um erro, imprima uma mensagem e encerre o script principal
        print(f"Erro ao executar {script}: {e}")
        raise SystemExit(1)
