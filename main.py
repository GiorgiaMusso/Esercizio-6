#Esempi type()
a = 2
b = "Gio"
c = True
d = complex(3,7)
e = (1,1,2)
f = 5.04
x = [a,b,c,d,e,f]
print("Esempi per la funzione type(): ")
print("Oggetti:")
print([i for i in x])
print("Tipo oggetti:")
print([type(i) for i in x])
#Esempi dir() 
import funzioni
print("Esempi per la funzione dir(): ")
print(dir(funzioni))
#Esempi help()
print("Esempi per la funzione help():")
import math
print(dir(math))
help(math.factorial)
help(funzioni.area_cerchio)
