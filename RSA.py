import random

# Calcular o máximo divisor comum (mdc) é o maior número inteiro que divide dois ou mais números inteiros sem deixar resto do valor a e b
def mdc(a, b): #Ela recebe dois números inteiros, "a" e "b", como parâmetros.
   while b:
       a, b = b, a % b
   return a

# Função para calcular o inverso multiplicativo
def InversoM(a, m):
    m0, x, y = m, 0, 1
    
    while a > 1:
        q = a // m # calcula o quociente inteiro
        m, a = a % m, m #resto da divisão, . Feito para continuar reduzindo o valor de "a" até que vire igual a 1.
        x, y = y - q * x, x #formula
    return y + m0 if y < 0 else y

# Função para verificar os números primos
def primo(n):
    if n < 2:
        return False
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            return False
    return True

# Função para gerar um par de chaves RSA com números primos fornecidos
def Gerar_Chaves(numeroPrimo, numeroPrimo2):
    n = numeroPrimo * numeroPrimo2
    Totiente = (numeroPrimo - 1) * (numeroPrimo2 - 1)

    # Escolher um valor aleatório para e, que seja co-primo com Totiente
    e = random.randint(2, Totiente - 1)
    while not primo(e) or mdc(e, Totiente) != 1:
        e = random.randint(2, Totiente - 1)

    d = InversoM(e, Totiente)  # Chave privada
    return ((e, n), (d, n))

# Função para criptografar uma mensagem
def Criptografar(ChavePublica, Mensagem):
    e, n = ChavePublica

    #mensagem_bytes = Mensagem.encode('utf-8')

    criptografar = [pow(ord(char), e, n) for char in Mensagem] 
    #cria uma lista
    #pow(base, expoente, [módulo]) numero elevado a potencia
    #"ord(char)" é o valor numérico do caractere na tabela ASCII "Código Padrão Americano para o Intercâmbio de Informação" poderia ter transformado em byte
    #operação de criptografia RSA --> Para cada caractere, calcula o valor do caractere elevado à potência e módulo n(produto dos dois numeros primos) usando a função pow(ord(char), e, n) com a chave publica

    return criptografar

# Função para descriptografar uma mensagem
def Descriptografar(ChavePrivada, criptografar):
    d, n = ChavePrivada
    descriptografar = [chr(pow(char, d, n)) for char in criptografar] #com a chave privada
    return ''.join(descriptografar)


# Função para gerar numeros primos aleatórios com parametros de intervalo de cada numero primo
def numeroPrimoAleat(Inicio, Fim):
    numero_primo = random.randint(Inicio, Fim)
    
    while not primo(numero_primo):
        numero_primo = random.randint(Inicio, Fim)

    return numero_primo


#Numeros Primos definidos, intervalo
numeroPrimo = numeroPrimoAleat(10, 50) 
numeroPrimo2 = numeroPrimoAleat(50, 100)


ChavePublica, ChavePrivada = Gerar_Chaves(numeroPrimo, numeroPrimo2)
print("Chave pública:", ChavePublica)
print("Chave privada:", ChavePrivada)

Opcao = int(input("Escolha 1 para criptografar ou 2 para descriptografar: "))
print("\nATENÇÃO !!!!!!!!!!!!!!!!!!")
print("Caso queira descriptografar guarde os dados da chave privada...")

if (Opcao == 1):

    mensagem = input("\nDigite a mensagem para criptografar: ")

    CriptografarMensagem = Criptografar(ChavePublica, mensagem)
    print(f"\nMensagem criptografada: {CriptografarMensagem}\n")

else:

    print("\nPara poder descriptografar é necessário a chave\n ")

    ChavePrivadaD = int(input("Digite o 1º valor da chave privada (da sessão do envio da mensagem): "))
    ChavePublicaN = int(input("Digite o 2º valor da chave privada (da mesma sessão): "))

    print("\n| Suas chaves são |")
    print("Chave pública:", ChavePublicaN)
    print("Chave privada:", ChavePrivadaD)
    
    ChavePrivada = (ChavePrivadaD, ChavePublicaN)

    # Descriptografar usando a chave privada 
    CriptografarMensagem = input("\nDigite a mensagem criptografada (separe os valores com vírgula e espaço): ").split(', ')
    CriptografarMensagem = [int(char) for char in CriptografarMensagem]
    
    DescriptografarMensagem = Descriptografar(ChavePrivada, CriptografarMensagem)
    print(f"\nMensagem descriptografada: {DescriptografarMensagem}\n")