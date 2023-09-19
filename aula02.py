#Variáveis primitivas

texto_string = 'um texto'
texto2_sting = 'segundo texto'

numericas_int = 5
numericas_float = 5.2

"""Comentário de multiplas linhas são 3 aspas duplas
    Posso continuar escrevendo o comentário
"""

#Python faz a verificação de tipo no operador +, sendo tanto pra concatenação quanto para adição
print(texto_string + texto2_sting)

#Escopo: determinado pelo espaçamento
if 10 > 2:
    print("Maior")  
print("Fora do escopo do if, FIM")      