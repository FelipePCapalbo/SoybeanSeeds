import subprocess
import os

# Caminho para o GraphHopper dentro do WSL
graphhopper_dir = "/home/felipe/graphhopper"
config_file = "config-example.yml"
java_opts = "-Xmx16g -Xms4g"

# Comando para rodar o GraphHopper no WSL
command = f"JAVA_OPTS='{java_opts}' java -jar web/target/graphhopper-web-11.0-SNAPSHOT.jar server {config_file}"

# Mudar para o diretório correto antes de rodar o comando

subprocess.Popen(command, shell=True, cwd=graphhopper_dir)
print("🚀 GraphHopper iniciado!")
