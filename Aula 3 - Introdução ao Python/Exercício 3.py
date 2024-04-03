time1 = input("Escreva o nome do time 1: ")
time2 = input("Escreva o nome do time 2: ")

gol1 = int(input(f"Quantos gols fez o {time1}: "))
gol2 = int(input(f"Quantos gols fez o {time2}: "))

if gol1>gol2:
   print(f"o time {time1} ganhou")
if gol2>gol1:
   print(f"o time {time2} ganhou")
else:
   print("Os dois times empataram!")

