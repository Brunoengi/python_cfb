#Escopo de variáveis e conceito de variável global

num1 = num2 = num3 = 0 #Todas as variáveis são globais
texto1 = 'um texto aleatorio'


def cn():
    print(texto1)

cn()

#Existe uma plavra reservada em python pra definir variáveis globais mesmo dentro de escopo de funções, a palavra reservada global

def qr():

    #Deve-se primeiro declarar a variável e atribuir na linha seguinte
    global varGlobal
    varGlobal = 'texto armazendo em uma variável global'

qr()
print(varGlobal)