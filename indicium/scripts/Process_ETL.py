import subprocess
from datetime import datetime

# Obtem a data atual no formato YYYY-MM-DD
data_atual = datetime.now().strftime('%Y-%m-%d')

# Caminho dos scripts spark-submit
script1 = "/indicium/scripts/extracao_dados_order_details.py"
script2 = "/indicium/scripts/process_order_details.py"
script3 = "/indicium/scripts/extracao_dados_orders.py"
script4 = "/indicium/scripts/process_orders.py"

# Lista de scripts a serem executados na ordem desejada
scripts_to_run = [
    f"spark-submit {script1} {data_atual}",
    f"spark-submit {script2} {data_atual}",
    f"spark-submit {script3} {data_atual}",
    f"spark-submit {script4} {data_atual}"
]

for script in scripts_to_run:
    try:
        # Execute o script usando subprocess.run
        subprocess.run(script, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        # Se ocorrer um erro, imprima uma mensagem e encerre o script principal
        print(f"Erro ao executar {script}: {e}")
        raise SystemExit(1)
