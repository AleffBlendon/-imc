# imc.py

# 1. Leitura de dados
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# 2. Cálculo do IMC
imc = peso / (altura ** 2)

# 3. Classificação segundo OMS
if imc < 18.5:
    categoria = "baixo peso"
elif imc < 25:
    categoria = "peso adequado"
elif imc < 30:
    categoria = "sobrepeso"
elif imc < 35:
    categoria = "obesidade grau I"
elif imc < 40:
    categoria = "obesidade grau II"
else:
    categoria = "obesidade grau III"

# 4. Exibir resultado
print(f"Seu IMC é {imc:.1f} kg/m²: {categoria}.")
