# Exercicio 2 - Crie programas que gerem um IndexError e um KeyError, explicando por que ocorreram

numeros = [1,2,3,4,5]
# print(numeros[5]) -> IndexError por que a lista tem 5 elementos (indice 0 ao 4) e tentei acessar o indice 5 que não existe

pessoas = {"nome":"Lucas","idade":"23"}
# print(pessoas["altura"]) -> KeyError pois a chave não existe no dict