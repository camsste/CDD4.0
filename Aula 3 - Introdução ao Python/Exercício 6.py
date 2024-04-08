mes = int(input("Coloque um número de 1 à 12 para ter o mês do ano correspondente: "))
if not mes <= 0 or mes > 12:
   if mes == 1:
      print(f"O mês é Janeiro")
   elif mes == 2:
      print(f"O mês é Fevereiro")
   elif mes == 3:
      print(f"O mês é Março")
   elif mes == 4:
      print(f"O mês é Abril")
   elif mes == 5:
      print(f"O mês é Maio")
   elif mes == 6:
      print(f"O mês é Junho")
   elif mes == 7:
      print(f"O mês é Julho")
   elif mes == 8:
      print(f"O mês é Agosto")
   elif mes == 9:
      print(f"O mês é Setembro")
   elif mes == 10:
      print(f"O mês é Outubro")
   elif mes == 11:
      print(f"O mês é Novembro")
   if mes == 12:
      print(f"O mês é Dezembro")

# Caso o número inserido pelo usuário não seja válido
if mes > 12 or mes < 1:
   print(f"O número inserido não é válido")
