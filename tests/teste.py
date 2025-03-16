import os

# 🔥 Código vulnerável (Execução de Comandos Arbitrários - RCE)
user_input = input("Digite um comando: ")
os.system(user_input)
