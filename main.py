#recebe velocidade do usuário
velocidade_usuario = int(input("Digite sua velocidade: "))

#seta variável vel_max
velocidade_maxima = 80

#compara valores
if velocidade_usuario <= velocidade_maxima:
  print("Nao recebeu multa")

if velocidade_usuario > velocidade_maxima:
  
  if velocidade_usuario <= velocidade_maxima + 10:
    print("Levou multa leve")
  
  elif velocidade_usuario > velocidade_maxima + 11 and velocidade_usuario <= velocidade_maxima + 20:
    print("Levou multa Grave")
  
  elif velocidade_usuario > velocidade_maxima + 21:
    print("Levou multa Gravíssima") 