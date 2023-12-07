import subprocess

# Lista de scripts a serem executados na ordem desejada
scripts_to_run = [
        "/indicium/scripts/extracao_dados_order_details.py"
        ]

for script in scripts_to_run:
    try:
        # Execute o script usando subprocess.run
        subprocess.run(["/indicium/scripts/extracao_dados_order_details.py", script], check=True)
    except subprocess.CalledProcessError as e:
        # Se ocorrer um erro, imprima uma mensagem e encerre o script principal
        print(f"Erro ao executar {script}: {e}")
        raise SystemExit(1)
