import subprocess
from datetime import datetime

# Obtem a data atual no formato YYYY-MM-DD
data_atual = datetime.now().strftime('%Y-%m-%d')

# Lista de scripts a serem executados na ordem desejada
scripts_to_run = [
        "spark-submit /indicium/scripts/extracao_dados_order_details.py {data_atual}"
        ]

for script in scripts_to_run:
    try:
        # Execute o script usando subprocess.run
        subprocess.run(["spark-submit /indicium/scripts/extracao_dados_order_details.py {data_atual}", script], check=True)
    except subprocess.CalledProcessError as e:
        # Se ocorrer um erro, imprima uma mensagem e encerre o script principal
        print(f"Erro ao executar {script}: {e}")
        raise SystemExit(1)
