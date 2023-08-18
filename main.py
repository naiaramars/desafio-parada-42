# 1) Faça um programa em que o usuário digita dois valores e o resultado da soma é exibido na tela. 
n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
soma = n1+n2

print(f"O resultado da soma é: {n1} + {n2}={soma}")

# 2) Faça um programa em que o usuário precisa cadastrar nome, idade, telefone e e-mail. Depois mostre os valores digitados na tela. 
nome = input("Digite o seu nome:")
idade = int(input("Digite sua idade:"))
telefone = int(input("Digite o seu telefone:"))
email = input("Digite seu e-mail:")

print(f"Os seus dados são: {nome},{idade}, {telefone}, {email}")

# 3) Faça um programa no qual o usuário precisa cadastrar as informações de um produto: código, nome, quantidade e preço. No final o programa deve mostrar as informações cadastradas e exibir o valor total da compra.
nome = input("Digite seu nome do produto:" )
codigo = input("Digite sua codigo do produto: ")
quantidade = float(input("Digite seu quantidade do produto: "))
preço = float(input("Digite seu preço do produto: "))

produto =[
    nome, codigo, quantidade, preço 
]

valor = quantidade * preço


print("Produto cadastrado foi:",produto)
print ("O valor final foi", valor)


# 4) Faça um programa que converte centímetros em metros. 
n1 = float(input("Digite quantos centimetros quer transformar em metros: "))

resultado = n1 / 100

print("convertendo tem " , resultado , "metros!" )

# 5) Faça um programa que calcule a área de um quadrado/retângulo.
base = float(input("Digite o tamanho da base da sua area: "))

altura = float(input("Digite a altura da sua area: "))

resultado = base * altura 

print("O tamanho total da sua area é: ",resultado)