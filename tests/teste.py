import os
import subprocess

user_input = input("Digite um comando: ")
os.system(user_input)  # 🚨 Deve ser detectado
subprocess.Popen(user_input, shell=True)  # 🚨 Deve ser detectado
eval("2+2")  # 🚨 Deve ser detectado
