import subprocess
from datetime import datetime

# Obtem a data atual no formato YYYY-MM-DD
data_atual = datetime.now().strftime('%Y-%m-%d')

# Caminhos dos scripts spark-submit
script1 = "/indicium/scripts/extracao_dados_customer_customer_demo.py"
script2 = "/indicium/scripts/process_customer_customer_demo.py"
script3 = "/indicium/scripts/extracao_dados_customer_demographics.py"
script4 = "/indicium/scripts/process_customer_demographics.py"
script5 = "/indicium/scripts/extracao_dados_customers.py"
script6 = "/indicium/scripts/process_customers.py"
script7 = "/indicium/scripts/extracao_dados_employee_territories.py"
script8 = "/indicium/scripts/process_employee_territories.py"
script9 = "/indicium/scripts/extracao_dados_employees.py"
script10 = "/indicium/scripts/process_employees.py"
script11 = "/indicium/scripts/extracao_dados_order_details.py"
script12 = "/indicium/scripts/process_order_details.py"
script13 = "/indicium/scripts/extracao_dados_orders.py"
script14 = "/indicium/scripts/process_orders.py"
script15 = "/indicium/scripts/extracao_dados_products.py"
script16 = "/indicium/scripts/process_products.py"
script17 = "/indicium/scripts/extracao_dados_region.py"
script18 = "/indicium/scripts/process_region.py"
script19 = "/indicium/scripts/extracao_dados_shippers.py"
script20 = "/indicium/scripts/process_shippers.py"
script21 = "/indicium/scripts/extracao_dados_suppliers.py"
script22 = "/indicium/scripts/process_suppliers.py"
script23 = "/indicium/scripts/extracao_dados_territories.py"
script24 = "/indicium/scripts/process_territories.py"
script25 = "/indicium/scripts/extracao_dados_us_states.py"
script26 = "/indicium/scripts/process_us_states.py"

# Lista de scripts a serem executados na ordem desejada
scripts_to_run = [
    f"spark-submit {script1} {data_atual}",
    f"spark-submit {script2} {data_atual}",
    f"spark-submit {script3} {data_atual}",
    f"spark-submit {script4} {data_atual}",
    f"spark-submit {script5} {data_atual}",
    f"spark-submit {script6} {data_atual}",
    f"spark-submit {script7} {data_atual}",
    f"spark-submit {script8} {data_atual}",
    f"spark-submit {script9} {data_atual}",
    f"spark-submit {script10} {data_atual}",
    f"spark-submit {script11} {data_atual}",
    f"spark-submit {script12} {data_atual}",
    f"spark-submit {script13} {data_atual}",
    f"spark-submit {script14} {data_atual}",
    f"spark-submit {script15} {data_atual}",
    f"spark-submit {script16} {data_atual}",
    f"spark-submit {script17} {data_atual}",
    f"spark-submit {script18} {data_atual}",
    f"spark-submit {script19} {data_atual}",
    f"spark-submit {script20} {data_atual}",
    f"spark-submit {script21} {data_atual}",
    f"spark-submit {script22} {data_atual}",
    f"spark-submit {script23} {data_atual}",
    f"spark-submit {script24} {data_atual}",
    f"spark-submit {script25} {data_atual}",
    f"spark-submit {script26} {data_atual}"
]

# Executa os scripts usando subprocess.run
for script in scripts_to_run:
    try:
        subprocess.run(script, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        # Se ocorrer um erro, imprima uma mensagem e encerre o script principal
        print(f"Erro ao executar {script}: {e}")
        raise SystemExit(1)
