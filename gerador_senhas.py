import random 
import string

print("=== Gerador de senhas seguras ===")

# perguntas ao usuário
tamanho = int(input("Qual o tamanho da senha? "))
maiusculas = input("Deseja incluir letras maiúsculas? (s/n): ").lower() == 's'
minusculas = input("Deseja incluir letras minúsculas? (s/n): ").lower() == 's'
numeros = input("Deseja incluir números? (s/n): ").lower() == 's'
simbolos = input("Deseja incluir símbolos? (s/n): ").lower() == 's'

# Monta a lista de caracteres possíveis
caracteres = ""

if maiusculas:
    caracteres += string.ascii_uppercase  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
if minusculas:
    caracteres += string.ascii_lowercase  # abcdefghijklmnopqrstuvwxyz
if numeros:
    caracteres += string.digits           # 0123456789
if simbolos:
    caracteres += string.punctuation      # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

if not caracteres:
    print("Você deve escolher pelo menos um tipo de caractere!")
    exit()

senha = ''.join(random.choice(caracteres) for _ in range(tamanho))

print(f"\nSua senha gerada: {senha}")

