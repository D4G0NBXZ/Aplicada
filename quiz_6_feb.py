A=float(input("Nota 1: "))
B=float(input("Nota 2: "))
C=float(input("Nota 3: "))


def prom(d1,d2,d3):
  #inicializacion de variables internas#
  nota_1=float()
  nota_2=float()
  #fin inicializacion#
  if d1>d2:
    nota_1=d1
    if d2>d3:
      nota_2=d2
    else:
      nota_2=d3
  else:
    nota_1=d2
    if d1>d3:
      nota_2=d1
    else:
      nota_2=d3
  #se agrega print para verificar numeros mayores#
  print("las notas mas altas son ", nota_1, " ",nota_2)
  nota_prom=(nota_1+nota_2)/2
  return (nota_prom)
#se agregan las variables en el llamado de la variable#
print("la nota promedio es ",prom(A,B,C))

