import os
print("\nEste programa calcula a area e o permetro de um triangulo qualquer!")
a = float(input("\nDigite o valor da primeira aresta: "))
b = float(input("\nDigite o valor da segunda aresta: "))
c = float(input("\nDigite o valor da terceira aresta: "))
h = float(input("\nDigite o valor da altura: "))
perimetro = int (a + b + c)
area = int (c * h / 2)
print("\n\nO valor do perimetro e igual a ",perimetro,", e area de",area,".")
print("\nObrigado por utilizar nosso sistema!")
os.system("pause")
